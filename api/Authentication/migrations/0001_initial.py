# Generated by Django 4.1.6 on 2023-03-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PhoneBook",
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
                ("phone", models.CharField(max_length=20, unique=True)),
                ("otp", models.CharField(max_length=10, unique=True)),
                ("verified", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
