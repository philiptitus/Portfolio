# Generated by Django 4.2.7 on 2024-11-29 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_jobexperience'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobexperience',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]