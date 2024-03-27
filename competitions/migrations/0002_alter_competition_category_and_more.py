# Generated by Django 5.0.3 on 2024-03-23 18:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("competitions", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="competition",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="competitions",
                to="competitions.category",
            ),
        ),
        migrations.AlterField(
            model_name="competition",
            name="created_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="competitions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="competition",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="competition_images"
            ),
        ),
    ]
