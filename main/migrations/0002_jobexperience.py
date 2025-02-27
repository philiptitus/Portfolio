# Generated by Django 4.2.7 on 2024-11-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(help_text='Title of the job, e.g., Software Engineer', max_length=100)),
                ('company_name', models.CharField(help_text='Name of the company', max_length=100)),
                ('location', models.CharField(blank=True, help_text='Location of the job (optional)', max_length=100, null=True)),
                ('start_date', models.DateField(help_text='Start date of the job')),
                ('end_date', models.DateField(blank=True, help_text='End date of the job. Leave blank if currently working', null=True)),
                ('description', models.TextField(help_text='Description of your responsibilities and achievements')),
                ('is_current', models.BooleanField(default=False, help_text='Check if this is your current job')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
    ]
