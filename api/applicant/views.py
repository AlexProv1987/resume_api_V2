from rest_framework.generics import RetrieveAPIView
from .serializers import ApplicantSerializer,GetApplicantSetSerializer
from .models import Applicant
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from rest_framework.views import APIView
from django.http import HttpResponse
import io
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK,HTTP_404_NOT_FOUND
# Create your views here.
class GetApplicant(RetrieveAPIView):
    queryset=Applicant.objects.all()
    serializer_class=ApplicantSerializer

class GetWidgetInfo(APIView):
    def get(self,request,pk,*args,**kwargs):
        applicant = Applicant.get_applicant_widget_info(pk)
        
        if applicant:
            serializer = GetApplicantSetSerializer(applicant)
            return Response(serializer.data,status=HTTP_200_OK)
        
        return Response({'message':'Not Found'},status=HTTP_404_NOT_FOUND)

class GetResume(APIView):
    
    def get(self,request,pk):
        return self.generate_pdf(request,pk)
        
    def generate_pdf(self,request,pk):
        
        applicant_context = Applicant.get_applicant_resume(pk)
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)

        #Custom Styles
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(
            name='SectionHeaderColored', 
            fontSize=16, 
            leading=16,
            fontName='Helvetica-Bold', textColor=HexColor("#6a5acd"),
            spaceAfter=10))
        styles.add(ParagraphStyle(
            name='SmallGray', 
            fontSize=9, 
            textColor=HexColor("#444444"))) 
        styles.add(ParagraphStyle(
            name='MediumGray', 
            fontSize=12, 
            textColor=HexColor("#444444"))) 
        styles.add(ParagraphStyle(
            name='LargeGray', 
            fontSize=14, 
            textColor=HexColor("#444444"))) 
        styles.add(ParagraphStyle(
            name='IndentedQuote',
            parent=styles['SmallGray'],
            leftIndent=16, 
            spaceBefore=2,
            spaceAfter=4))
        
        content = []
      
        #Header
        content.extend(self._render_header(applicant_context, styles))
        
        #Employment
        content.append(Paragraph("Employment", styles['SectionHeaderColored']))
        for job in applicant_context.work.all().order_by('order'):
            to_date_display = job.to_date if job.to_date else "Current"
            content.append(Paragraph(f"<b>{job.employer_name}</b>", styles['MediumGray']))
            content.append(Paragraph(f"<i>{job.job_title}</i>", styles['SmallGray']))
            content.append(Spacer(1, 1))
            content.append(Paragraph(f"{job.from_date}-{to_date_display}", styles['SmallGray']))
            content.append(Spacer(1, 1))
            for point in job.work_details.all().order_by('order'):
                content.append(Paragraph(f"➤ {point.work_detail_text}", styles['SmallGray']))
            content.append(Spacer(1, 6))
        
        #Awards
        if applicant_context.awards.exists():
            content.append(Paragraph("Awards & Recognition", styles["SectionHeaderColored"]))
            for award in applicant_context.awards.all().order_by('order'):
                content.append(Paragraph(f"• {award.reward_name}", styles["SmallGray"]))
            content.append(Spacer(1, 10))

        
        #Certifications
        if applicant_context.certifications.exists():
            content.append(Paragraph("Certifications", styles["SectionHeaderColored"]))
            for cert in applicant_context.certifications.all().order_by('order'):
                content.append(Paragraph(f"• {cert.name}", styles["SmallGray"]))
            content.append(Spacer(1, 10))
        
        #Skills
        if applicant_context.skills.exists():
            content.append(Paragraph("Skills", styles["SectionHeaderColored"]))
            skills_line = " | ".join(skill.skill_name for skill in applicant_context.skills.all().order_by('order'))
            content.append(Paragraph(skills_line, styles["SmallGray"]))
            content.append(Spacer(1, 10))
        
        #Education
        if applicant_context.education.exists():
            content.append(Paragraph("Education", styles["SectionHeaderColored"]))
            for edu in applicant_context.education.all().order_by('order'):
                content.append(Paragraph(
                    f"• {edu.name}<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-{edu.get_education_level_display()}", styles["SmallGray"]
                ))
                if edu.area_of_study:
                    content.append(Paragraph(
                    f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-{edu.area_of_study}", styles["SmallGray"]
                ))
            content.append(Spacer(1, 10))
        
        #References
        if applicant_context.references.exists():
            content.append(Paragraph("References", styles["SectionHeaderColored"]))
            for refer in applicant_context.references.all().order_by('order'):
                content.append(Paragraph(
                    f"• {refer.name}<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{refer.relation} - {refer.job_title}", styles["SmallGray"]
                ))
                if refer.reference_recommendation:
                    content.append(Paragraph(
                    f"<i>{refer.reference_recommendation}</i>", styles["IndentedQuote"]
                ))
            content.append(Spacer(1, 10))
            
        content.append(PageBreak())
        
        #Projects
        if applicant_context.projects.exists():
            content.append(Paragraph("Projects", styles['SectionHeaderColored']))
            for project in applicant_context.projects.all().order_by('order'):
            
                content.append(Paragraph(f"<b>{project.name}</b>", styles['MediumGray']))
                content.append(Spacer(1, 2))
                
                link_parts = []
                if project.source_control_url:
                    link_parts.append(f'<a href="{project.source_control_url}" color="blue"><b>Git</b></a>')

                if project.video_url:
                    link_parts.append(f'<a href="{project.video_url}" color="blue"><b>Video</b></a>')

                if project.demo_url:
                    link_parts.append(f'<a href="{project.demo_url}" color="blue"><b>Demo</b></a>')
                    
                joined_links = " | ".join(link_parts)
                
                if joined_links:
                    content.append(Paragraph(joined_links, styles['SmallGray']))
                    
                content.append(Paragraph(f"<i>{project.description}</i>", styles['SmallGray']))
                
                content.append(Spacer(1, 6))
                '''I just dont like the concept of this tbh'''
                '''
                for point in project.project_details.all().order_by('order'):
                    content.append(Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;➤ {point.detail_text}", styles['SmallGray']))
                '''   
            content.append(Spacer(1, 6))
            
        doc.build(content)
        buffer.seek(0)
        
        return HttpResponse(
            buffer,
            content_type='application/pdf',
            headers={
                'Content-Disposition': 'inline; filename="generated.pdf"',
            },
        )
    
    def _render_header(self,profile, styles):
        elems = []

        img_path = profile.applicant_photo
        image = Image(img_path, width=90, height=90)
        image.hAlign = 'LEFT'

        bio = Paragraph(profile.applicant_bio, styles['SmallGray'])

        header_table = Table(
            [[image, bio]],
            colWidths=[100, 440],
            style=TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")])
        )
        elems.append(header_table)
        #eh 
        #elems.append(FullPageBar(HexColor("#d0c4f7"), height=25))
        elems.append(Spacer(1, 12))
        return elems
