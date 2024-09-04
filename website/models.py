from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    content = models.TextField()
    
    class Meta:
        verbose_name_plural = "Articles"
        
    def __str__(self):
        return self.content

class HomeBlog(models.Model):
    title = models.CharField(max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='homeblog_img')
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_img')
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = "Home Blogs"
        
    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_img')
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_img')
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name_plural = "Blogs"
        
    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    
    class Meta:
        verbose_name_plural = "Contacts"
        
    def __str__(self):
        return self.name
    
class OurWork(models.Model):
    image = models.ImageField(upload_to='project-img')
    title = models.CharField(max_length=100)
    link = models.URLField()
    
    class Meta:
        verbose_name_plural = "Our works"
        
    def __str__(self):
        return self.title
    
class NewsLetter(models.Model):
    email = models.EmailField()
    
    class Meta:
        verbose_name_plural = "Newsletters"
        
    def __str__(self):
        return self.email
    
class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimonial-img')
    name = models.CharField(max_length=100)
    content = models.TextField()
    
    class Meta:
        verbose_name_plural = "Testimonials"
        
    def __str__(self):
        return self.name
    

class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    project_type = models.CharField(max_length=200)
    project_description = models.TextField()
    existing_website = models.CharField(max_length=200)
    desired_deadline = models.CharField(max_length=20)
    estimated_budget = models.CharField(max_length=20)
    preferred_start_date = models.CharField(max_length=20)
    additional_notes = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Bookings"
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Team(models.Model):
    image = models.ImageField(upload_to='team-img')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    facebook_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    tiktok_link = models.URLField(null=True, blank=True)
    x_link = models.URLField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    website_link = models.URLField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Our Team"
        
    def __str__(self):
        return f"{self.name} - {self.position}"