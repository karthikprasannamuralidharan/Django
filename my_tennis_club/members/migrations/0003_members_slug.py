# Generated by Django 4.1.7 on 2023-04-01 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_members_dob_members_rollno'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
