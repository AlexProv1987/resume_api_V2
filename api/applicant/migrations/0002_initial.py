# Generated by Django 5.2.3 on 2025-06-21 23:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("applicant", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="applicant",
            name="user_reltn",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
        migrations.AddField(
            model_name="applicantcontactmethods",
            name="applicant_reltn",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contact_method",
                to="applicant.applicant",
                verbose_name="Applicant",
            ),
        ),
        migrations.AddField(
            model_name="applicantsocials",
            name="applicant_reltn",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="social",
                to="applicant.applicant",
                verbose_name="Applicant",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="applicantcontactmethods",
            unique_together={("applicant_reltn", "contact_type")},
        ),
        migrations.AlterUniqueTogether(
            name="applicantsocials",
            unique_together={("applicant_reltn", "platform")},
        ),
    ]
