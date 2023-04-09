# Generated by Django 4.1.7 on 2023-04-08 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='account_type',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='rating',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/profile/'),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
