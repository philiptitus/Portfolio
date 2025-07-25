from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    name = models.CharField(max_length=100, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    name_embedding = models.TextField(blank=True, null=True)  # Embedding for 'name'
    image = models.FileField(blank=True, null=True, upload_to="skills")
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    bio_embedding = models.TextField(blank=True, null=True)  # Embedding for 'bio'
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class ContactProfile(models.Model):


    CATEGORY = [
        ('DATA SCIENCE.AI AND ML', 'DATA SCIENCE.AI AND ML'),
        ('WEB DEVELOPMENT', 'WEB DEVELOPMENT'),
        ('MOBILE DEVELOPMENT', 'MOBILE DEVELOPMENT'),
        ('CYBERSECURITY', 'CYBERSECURITY'),
        ('CLOUD COMPUTING', 'CLOUD COMPUTING'),
        ('GAME DEVELOPMENT', 'GAME DEVELOPMENT'),
        ('OTHER', 'OTHER'),





    ]

    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    category = models.CharField(max_length=264, choices=CATEGORY, default='WEB DEVELOPMENT')
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'






class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]

    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)
    def __str__(self):
        return self.name


class Portfolio(models.Model):
    CATEGORY = [
        ('DATA SCIENCE.AI AND ML', 'DATA SCIENCE.AI AND ML'),
        ('WEB DEVELOPMENT', 'WEB DEVELOPMENT'),
        ('MOBILE DEVELOPMENT', 'MOBILE DEVELOPMENT'),
        ('CYBERSECURITY', 'CYBERSECURITY'),
        ('CLOUD COMPUTING', 'CLOUD COMPUTING'),
        ('GAME DEVELOPMENT', 'GAME DEVELOPMENT'),
        ('OTHER', 'OTHER'),
    ]

    STATUS_SKILLS = [
        ('PYTHON', 'PYTHON'),
        ('JAVASCRIPT', 'JAVASCRIPT'),
        ('HTML & CSS', 'HTML & CSS'),
        ('PHP', 'PHP'),
        ('JAVA', 'JAVA'),
        ('C++', 'C++'),
        ('REACT NATIVE', 'REACT NATIVE'),
        ('DJANGO', 'DJANGO'),
        ('DJANGO + REACT', 'DJANGO + REACT'),
        ('DJANGO + REACT NATIVE', 'DJANGO + REACT NATIVE'),
    ]

    TIER_CHOICES = [
        ('S', 'S'),
        ('A', 'A'),
        ('B', 'B'),
    ]

    class Meta:
        verbose_name_plural = 'Portfolios'
        verbose_name = 'Portfolio'
        ordering = ["name"]

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    name_embedding = models.TextField(blank=True, null=True)  # Embedding for 'name'
    description = models.CharField(max_length=500, blank=True, null=True)
    description_embedding = models.TextField(blank=True, null=True)  # Embedding for 'description'
    body = RichTextField(blank=True, null=True)
    body_embedding = models.TextField(blank=True, null=True)  # Embedding for 'body'
    url = models.URLField(blank=True, null=True,)
    core_skill = models.CharField(max_length=264, choices=STATUS_SKILLS, default='PYTHON')
    category = models.CharField(max_length=264, choices=CATEGORY, default='WEB DEVELOPMENT')
    tier = models.CharField(max_length=1, choices=TIER_CHOICES, default='A')  # New tier field
    image_url = models.URLField(null=True, blank=True)
    imager_url = models.URLField(null=True, blank=True)
    image2_url = models.URLField(null=True, blank=True)
    image3_url = models.URLField(null=True, blank=True)
    image4_url = models.URLField(null=True, blank=True)
    image5_url = models.URLField(null=True, blank=True)
    image6_url = models.URLField(null=True, blank=True)
    image7_url = models.URLField(null=True, blank=True)
    image8_url = models.URLField(null=True, blank=True)
    image9_url = models.URLField(null=True, blank=True)
    image10_url = models.URLField(null=True, blank=True)
    url_2 = models.URLField(default="https://github.com/philiptitus/todoapp2.0.git")
    url_3 = models.URLField(default="https://github.com/philiptitus/todoapp2.0.git")
    amazon_url = models.URLField(blank=True, null=True,)
    star = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    skills = models.ManyToManyField(Skill, related_name='portfolios', blank=True)
    video_url = models.URLField(blank=True, null=True)
    is_api = models.BooleanField(default=True)
    is_live = models.BooleanField(default=True)
    app = models.FileField(upload_to='apk', blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


class MLModel(models.Model):
    CATEGORY = [
        ('SUPERVISED_LEARNING', 'Supervised Learning'),
        ('UNSUPERVISED_LEARNING', 'Unsupervised Learning'),
        ('REINFORCEMENT_LEARNING', 'Reinforcement Learning'),
        ('DEEP_LEARNING', 'Deep Learning'),
        ('NATURAL_LANGUAGE_PROCESSING', 'Natural Language Processing'),
        ('COMPUTER_VISION', 'Computer Vision'),
        ('TIME_SERIES', 'Time Series Analysis'),
        ('RECOMMENDATION_SYSTEMS', 'Recommendation Systems'),
        ('ANOMALY_DETECTION', 'Anomaly Detection'),
        ('CLUSTERING', 'Clustering'),
    ]

    ML_SKILLS = [
        ('SCIKIT_LEARN', 'Scikit-Learn'),
        ('TENSORFLOW', 'TensorFlow'),
        ('PYTORCH', 'PyTorch'),
        ('KERAS', 'Keras'),
        ('NUMPY', 'NumPy'),
        ('PANDAS', 'Pandas'),
        ('OPENCV', 'OpenCV'),
        ('NLTK', 'NLTK'),
        ('SPACY', 'SpaCy'),
        ('XGBOOST', 'XGBoost'),
        ('LIGHTGBM', 'LightGBM'),
        ('TRANSFORMERS', 'Transformers'),
    ]

    TIER_CHOICES = [
        ('S', 'S'),
        ('A', 'A'),
        ('B', 'B'),
    ]

    class Meta:
        verbose_name_plural = 'ML Models'
        verbose_name = 'ML Model'
        ordering = ["name"]

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    name_embedding = models.TextField(blank=True, null=True)  # Embedding for 'name'
    body = RichTextField(blank=True, null=True)
    body_embedding = models.TextField(blank=True, null=True)  # Embedding for 'body'
    category = models.CharField(max_length=264, choices=CATEGORY, default='SUPERVISED_LEARNING')
    tier = models.CharField(max_length=1, choices=TIER_CHOICES, default='A')
    image = models.ImageField(upload_to='ml_models', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='ml_models', blank=True)
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(MLModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/ml-model/{self.slug}"


class Project(models.Model):
    CATEGORY = [
        ('DATA SCIENCE.AI AND ML', 'DATA SCIENCE.AI AND ML'),
        ('WEB DEVELOPMENT', 'WEB DEVELOPMENT'),
        ('MOBILE DEVELOPMENT', 'MOBILE DEVELOPMENT'),
        ('CYBERSECURITY', 'CYBERSECURITY'),
        ('CLOUD COMPUTING', 'CLOUD COMPUTING'),
        ('GAME DEVELOPMENT', 'GAME DEVELOPMENT'),
        ('OTHER', 'OTHER'),





    ]



    STATUS_CHOICES = [
        ('complete', 'Complete'),
        ('almost there', 'Almost There'),
        ('just started recently', 'Just Started'),
    ]
    STATUS_SKILLS = [
        ('PYTHON', 'PYTHON'),
        ('JAVASCRIPT', 'JAVASCRIPT'),
        ('HTML & CSS', 'HTML & CSS'),
        ('PHP', 'PHP'),
        ('JAVA', 'JAVA'),
        ('C++', 'C++'),




    ]


    class Meta:
        verbose_name_plural = 'Upcoming Projects'
        verbose_name = 'Upcoming Project'
        ordering = ['date']

    date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=264)
    name_embedding = models.TextField(blank=True, null=True)  # Embedding for 'name'
    status = models.CharField(max_length=1000, choices=STATUS_CHOICES, default='Just Started')
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    imager = models.ImageField(blank=True, null=True, upload_to="blog")
    core_skill = models.CharField(max_length=264, choices=STATUS_SKILLS, default='PYTHON')
    category = models.CharField(max_length=264, choices=CATEGORY, default='WEB DEVELOPMENT')
    url = models.URLField(default="https://github.com/philiptitus/todoapp2.0.git")
    description = models.TextField(max_length=1000, blank=True, null=True)
    description_embedding = models.TextField(blank=True, null=True)  # Embedding for 'description'
    body = RichTextField(blank=True, null=True)
    body_embedding = models.TextField(blank=True, null=True)  # Embedding for 'body'
    # skills = models.ManyToManyField(Skill, blank=True)
    for_sale = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/project/{self.slug}"









class Blog(models.Model):
    CATEGORY = [
        ('DATA SCIENCE.AI AND ML', 'DATA SCIENCE.AI AND ML'),
        ('WEB DEVELOPMENT', 'WEB DEVELOPMENT'),
        ('MOBILE DEVELOPMENT', 'MOBILE DEVELOPMENT'),
        ('CYBERSECURITY', 'CYBERSECURITY'),
        ('CLOUD COMPUTING', 'CLOUD COMPUTING'),
        ('GAME DEVELOPMENT', 'GAME DEVELOPMENT'),
        ('OTHER', 'OTHER'),





    ]

    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    name_embedding = models.TextField(blank=True, null=True)  # Embedding for 'name'
    description = models.CharField(max_length=500, blank=True, null=True)
    description_embedding = models.TextField(blank=True, null=True)  # Embedding for 'description'
    body = RichTextField(blank=True, null=True)
    body_embedding = models.TextField(blank=True, null=True)  # Embedding for 'body'
    png_url=models.URLField(null=True, blank=True)
    category = models.CharField(max_length=264, choices=CATEGORY, default='WEB DEVELOPMENT')
    slug = models.SlugField(null=True, blank=True)
    image_url=models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"


class Certificate(models.Model):
    CATEGORY = [
        ('DATA SCIENCE.AI AND ML', 'DATA SCIENCE.AI AND ML'),
        ('WEB DEVELOPMENT', 'WEB DEVELOPMENT'),
        ('MOBILE DEVELOPMENT', 'MOBILE DEVELOPMENT'),
        ('CYBERSECURITY', 'CYBERSECURITY'),
        ('CLOUD COMPUTING', 'CLOUD COMPUTING'),
        ('GAME DEVELOPMENT', 'GAME DEVELOPMENT'),
        ('OTHER', 'OTHER'),





    ]

    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_embedding = models.TextField(blank=True, null=True)  # Embedding for 'name'
    title = models.CharField(max_length=200, blank=True, null=True)
    title_embedding = models.TextField(blank=True, null=True)  # Embedding for 'title'
    description = models.CharField(max_length=500, blank=True, null=True)
    description_embedding = models.TextField(blank=True, null=True)  # Embedding for 'description'
    is_active = models.BooleanField(default=True)
    is_ongoing = models.BooleanField(default=True)
    image_url = models.URLField(null=True, blank=True)
    url = models.URLField(blank=True, null=True)



    def __str__(self):
        return self.name




class Award(models.Model):
    class Meta:
        verbose_name_plural = 'Awards'
        verbose_name = 'Award'

    date = models.DateTimeField(blank=True, null=True)
    issued_by = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    title_embedding = models.TextField(blank=True, null=True)  # Embedding for 'title'
    description = models.CharField(max_length=500, blank=True, null=True)
    description_embedding = models.TextField(blank=True, null=True)  # Embedding for 'description'
    is_active = models.BooleanField(default=True)
    image_url = models.URLField(null=True, blank=True)



    def __str__(self):
        return self.title





class WebhookEvent(models.Model):
    event_type = models.CharField(max_length=100)
    description = models.TextField()
    repository = models.CharField(max_length=255)
    repository_url = models.URLField()
    commit_url = models.URLField()
    pusher = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_type} - {self.repository}"



class Video(models.Model):
    class Meta:
        verbose_name_plural = 'Videos'
        verbose_name = 'Video'



    url = models.URLField(blank=True, null=True)
    text = models.CharField(max_length=264)
    description = models.TextField(max_length=1000)







from django.db import models

class JobExperience(models.Model):
    job_title = models.CharField(max_length=100, help_text="Title of the job, e.g., Software Engineer")
    job_title_embedding = models.TextField(blank=True, null=True)  # Embedding for 'job_title'
    company_name = models.CharField(max_length=100, help_text="Name of the company")
    company_name_embedding = models.TextField(blank=True, null=True)  # Embedding for 'company_name'
    location = models.CharField(max_length=100, blank=True, null=True, help_text="Location of the job (optional)")
    location_embedding = models.TextField(blank=True, null=True)  # Embedding for 'location'
    start_date = models.DateField(help_text="Start date of the job")
    end_date = models.DateField(blank=True, null=True, help_text="End date of the job. Leave blank if currently working")
    description = models.TextField(help_text="Description of your responsibilities and achievements")
    description_embedding = models.TextField(blank=True, null=True)  # Embedding for 'description'
    is_current = models.BooleanField(default=False, help_text="Check if this is your current job")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

    class Meta:
        ordering = ['-start_date']
