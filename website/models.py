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