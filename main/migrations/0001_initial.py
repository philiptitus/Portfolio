# Generated by Django 4.2.7 on 2024-11-22 10:54

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('issued_by', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Award',
                'verbose_name_plural': 'Awards',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('png_url', models.URLField(blank=True, null=True)),
                ('category', models.CharField(choices=[('DATA SCIENCE.AI AND ML', 'DATA SCIENCE.AI AND ML'), ('WEB DEVELOPMENT', 'WEB DEVELOPMENT'), ('MOBILE DEVELOPMENT', 'MOBILE DEVELOPMENT'), ('CYBERSECURITY', 'CYBERSECURITY'), ('CLOUD COMPUTING', 'CLOUD COMPUTING'), ('GAME DEVELOPMENT', 'GAME DEVELOPMENT'), ('OTHER', 'OTHER')], default='WEB DEVELOPMENT', max_length=264)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog Profiles',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(choices=[('DATA SCIENCE.AI AND ML', 'DATA SCIENCE.AI AND ML'), ('WEB DEVELOPMENT', 'WEB DEVELOPMENT'), ('MOBILE DEVELOPMENT', 'MOBILE DEVELOPMENT'), ('CYBERSECURITY', 'CYBERSECURITY'), ('CLOUD COMPUTING', 'CLOUD COMPUTING'), ('GAME DEVELOPMENT', 'GAME DEVELOPMENT'), ('OTHER', 'OTHER')], default='WEB DEVELOPMENT', max_length=264)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_ongoing', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Certificate',
                'verbose_name_plural': 'Certificates',
            },
        ),
        migrations.CreateModel(
            name='ContactProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('category', models.CharField(choices=[('DATA SCIENCE.AI AND ML', 'DATA SCIENCE.AI AND ML'), ('WEB DEVELOPMENT', 'WEB DEVELOPMENT'), ('MOBILE DEVELOPMENT', 'MOBILE DEVELOPMENT'), ('CYBERSECURITY', 'CYBERSECURITY'), ('CLOUD COMPUTING', 'CLOUD COMPUTING'), ('GAME DEVELOPMENT', 'GAME DEVELOPMENT'), ('OTHER', 'OTHER')], default='WEB DEVELOPMENT', max_length=264)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Contact Profile',
                'verbose_name_plural': 'Contact Profiles',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('url', models.URLField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('is_image', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Media Files',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=264)),
                ('status', models.CharField(choices=[('complete', 'Complete'), ('almost there', 'Almost There'), ('just started recently', 'Just Started')], default='Just Started', max_length=1000)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='portfolio')),
                ('imager', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('core_skill', models.CharField(choices=[('PYTHON', 'PYTHON'), ('JAVASCRIPT', 'JAVASCRIPT'), ('HTML & CSS', 'HTML & CSS'), ('PHP', 'PHP'), ('JAVA', 'JAVA'), ('C++', 'C++')], default='PYTHON', max_length=264)),
                ('category', models.CharField(choices=[('DATA SCIENCE.AI AND ML', 'DATA SCIENCE.AI AND ML'), ('WEB DEVELOPMENT', 'WEB DEVELOPMENT'), ('MOBILE DEVELOPMENT', 'MOBILE DEVELOPMENT'), ('CYBERSECURITY', 'CYBERSECURITY'), ('CLOUD COMPUTING', 'CLOUD COMPUTING'), ('GAME DEVELOPMENT', 'GAME DEVELOPMENT'), ('OTHER', 'OTHER')], default='WEB DEVELOPMENT', max_length=264)),
                ('url', models.URLField(default='https://github.com/philiptitus/todoapp2.0.git')),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('for_sale', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Upcoming Project',
                'verbose_name_plural': 'Upcoming Projects',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('score', models.IntegerField(blank=True, default=80, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='skills')),
                ('is_key_skill', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('text', models.CharField(max_length=264)),
                ('description', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='WebhookEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('repository', models.CharField(max_length=255)),
                ('repository_url', models.URLField()),
                ('commit_url', models.URLField()),
                ('pusher', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv')),
                ('skills', models.ManyToManyField(blank=True, to='main.skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('core_skill', models.CharField(choices=[('PYTHON', 'PYTHON'), ('JAVASCRIPT', 'JAVASCRIPT'), ('HTML & CSS', 'HTML & CSS'), ('PHP', 'PHP'), ('JAVA', 'JAVA'), ('C++', 'C++'), ('REACT NATIVE', 'REACT NATIVE'), ('DJANGO', 'DJANGO'), ('DJANGO + REACT', 'DJANGO + REACT'), ('DJANGO + REACT NATIVE', 'DJANGO + REACT NATIVE')], default='PYTHON', max_length=264)),
                ('category', models.CharField(choices=[('DATA SCIENCE.AI AND ML', 'DATA SCIENCE.AI AND ML'), ('WEB DEVELOPMENT', 'WEB DEVELOPMENT'), ('MOBILE DEVELOPMENT', 'MOBILE DEVELOPMENT'), ('CYBERSECURITY', 'CYBERSECURITY'), ('CLOUD COMPUTING', 'CLOUD COMPUTING'), ('GAME DEVELOPMENT', 'GAME DEVELOPMENT'), ('OTHER', 'OTHER')], default='WEB DEVELOPMENT', max_length=264)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('imager_url', models.URLField(blank=True, null=True)),
                ('image2_url', models.URLField(blank=True, null=True)),
                ('image3_url', models.URLField(blank=True, null=True)),
                ('image4_url', models.URLField(blank=True, null=True)),
                ('image5_url', models.URLField(blank=True, null=True)),
                ('image6_url', models.URLField(blank=True, null=True)),
                ('image7_url', models.URLField(blank=True, null=True)),
                ('image8_url', models.URLField(blank=True, null=True)),
                ('image9_url', models.URLField(blank=True, null=True)),
                ('image10_url', models.URLField(blank=True, null=True)),
                ('url_2', models.URLField(default='https://github.com/philiptitus/todoapp2.0.git')),
                ('url_3', models.URLField(default='https://github.com/philiptitus/todoapp2.0.git')),
                ('amazon_url', models.URLField(blank=True, null=True)),
                ('star', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('app', models.FileField(blank=True, null=True, upload_to='apk')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('skills', models.ManyToManyField(blank=True, related_name='portfolios', to='main.skill')),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios',
                'ordering': ['name'],
            },
        ),
    ]
