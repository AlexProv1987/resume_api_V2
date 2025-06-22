from openai import OpenAI
from django.conf import settings
from api.applicant.models import Applicant
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_404_NOT_FOUND
# Create your views here.
class AskQuestion(APIView):

    client = OpenAI(
    api_key = settings.OPEN_AI_KEY if settings.OPEN_AI_KEY else "your_mom_420",
    organization='org-0sHye0dWY66aYcalIkA74kOG'
    )
    
    def post(self,request,*args,**kwargs):
        applicant = Applicant.get_applicant_resume(request.data.get('applicant',None))
        
        if applicant is None:
            return Response({},status=HTTP_404_NOT_FOUND)
        
        context = self.generate_applicant_context(applicant)
        
        try:
            answer = self.ask_chatgpt(context,request.data.get('question',None))
            return Response({'answer':answer},status=HTTP_200_OK) 
        except:
            return Response({'answer':'There appears to be an issue with OpenAI Currently. Please Try again later!'},status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    def generate_applicant_context(self,applicant:Applicant):
        lines = []
    
        lines.append("=== Applicant Summary ===")
        lines.append(f"Name: {applicant.user_reltn.first_name} {applicant.user_reltn.last_name}")
        lines.append(f"Current Title: {applicant.current_title or 'N/A'}")
        lines.append(f"Open to Work: {'Yes' if applicant.accepting_work else 'No'}")
        lines.append("Biography:")
        lines.append(applicant.applicant_bio or "N/A")
        lines.append("")

        if applicant.skills.exists():
            lines.append("=== Skills ===")
            for skill in applicant.skills.all():
                lines.append(f"- {skill.skill_name} ({skill.years_of_experience} yrs)")
            lines.append("")

        if applicant.education.exists():
            lines.append("=== Education ===")
            for edu in applicant.education.all():
                lines.append(f"{edu.area_of_study or 'General'} - {edu.name} ({edu.from_date.year}–{edu.to_date.year if edu.to_date else 'Present'})")
            lines.append("")

        if applicant.work.exists():
            lines.append("=== Work History ===")
            for work in applicant.work.all():
                lines.append(f"{work.job_title} at {work.employer_name} ({work.from_date}–{work.to_date or 'Current'})")
                for detail in work.work_details.all():
                    lines.append(f"- {detail.work_detail_text}")
            lines.append("")

        if applicant.projects.exists():
            lines.append("=== Projects ===")
            for project in applicant.projects.all():
                lines.append(f"Project: {project.name}")
                lines.append(f"- {project.description}")
                for detail in project.project_details.all():
                    lines.append(f"- {detail.detail_text}")
            lines.append("")
    
        if applicant.context.exists():
            lines.append("=== Additional Information ===")
            for context in applicant.context.all():
                lines.append(f"- {context.context_text}")
        return "\n".join(lines)

    def ask_chatgpt(self,context:str,prompt: str) -> str:
        response = self.client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are assisting a potential employer asking questions about this. If this is not related to employment let them know you are not able to assist. Answer in 6 sentences or less."},
            {"role": "user", "content": context},
            {"role": "user", "content": prompt}
        ])
        return response.choices[0].message.content
