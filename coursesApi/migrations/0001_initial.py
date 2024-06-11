# Generated by Django 4.2.6 on 2023-11-16 23:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("course_program", models.CharField(max_length=50)),
                ("course_code", models.CharField()),
                ("course_name", models.CharField(max_length=255)),
                ("elective", models.BooleanField()),
            ],
        ),
    ]