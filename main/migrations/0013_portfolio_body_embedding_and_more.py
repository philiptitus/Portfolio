# Generated by Django 4.2.7 on 2025-07-12 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_userprofile_bio_embedding'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='body_embedding',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='description_embedding',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='name_embedding',
            field=models.TextField(blank=True, null=True),
        ),
    ]
