# Generated by Django 4.1.3 on 2022-12-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_tag_project_vote_ratio_project_vote_total_review_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="featured_image",
            field=models.ImageField(
                blank=True, default="default.jpeg", null=True, upload_to=""
            ),
        ),
    ]
