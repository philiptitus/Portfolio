# Generated by Django 4.2.7 on 2025-07-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_skill_name_embedding'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio_embedding',
            field=models.TextField(blank=True, null=True),
        ),
    ]
