# Generated by Django 5.0.1 on 2024-02-22 10:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profile1", "0005_alter_experience_projects"),
    ]

    operations = [
        migrations.AddField(
            model_name="experience",
            name="companyImage",
            field=models.ImageField(null=True, upload_to="images/"),
        ),
    ]
