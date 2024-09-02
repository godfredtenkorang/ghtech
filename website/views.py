from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.
def index(request):
    homeblogs = Blog.objects.all()[:3]
    our_works = OurWork.objects.all()[:4]
    testimonials = Testimonial.objects.all()
    if request.method == 'POST':
        email = request.POST['email']
        
        newsletter = NewsLetter(email=email)
        newsletter.save()
        return redirect('index')
    context = {
        'homeblogs': homeblogs,
        'our_works': our_works,
        'testimonials': testimonials
    }
    return render(request, 'website/index.html', context)

def aboutUs(request):
    if request.method == 'POST':
        email = request.POST['email']
        
        newsletter = NewsLetter(email=email)
        newsletter.save()
        return redirect('aboutUs')
    
    context = {
        'title': 'About Us'
    }
    return render(request, 'website/about-us.html', context)

def blog(request):
    blogs = Blog.objects.all()
    if request.method == 'POST':
        email = request.POST['email']
        
        newsletter = NewsLetter(email=email)
        newsletter.save()
        return redirect('blog')
    context = {
        'blogs': blogs,
        'title': 'Blogs'
    }
    return render(request, 'website/blog.html', context)

# def blogDetail(request, blog_slug):
#     homeblog = get_object_or_404(HomeBlog, slug=blog_slug)
#     context = {
#         'homeblog': homeblog,
#         'title': 'Blog Details'
#     }
#     return render(request, 'website/blogDetail.html', context)

def blogPostDetail(request, post_slug):
    blog = get_object_or_404(Blog, slug=post_slug)
    if request.method == 'POST':
        email = request.POST['email']
        
        newsletter = NewsLetter(email=email)
        newsletter.save()
        return redirect('blog_detail')
    context = {
        'blog': blog,
        'title': 'Blog Details'
    }
    return render(request, 'website/blogPost_detail.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        return redirect('contact')
    context = {
        'title': 'Contact'
    }
    return render(request, 'website/contact-us.html', context)

def ourWork(request):
    our_works = OurWork.objects.all()
    if request.method == 'POST':
        email = request.POST['email']
        
        newsletter = NewsLetter(email=email)
        newsletter.save()
        return redirect('ourWork')
    context = {
        'our_works': our_works,
        'title': 'Our Works'
    }
    return render(request, 'website/ourWork.html', context)

def service(request):
    if request.method == 'POST':
        email = request.POST['email']
        
        newsletter = NewsLetter(email=email)
        newsletter.save()
        return redirect('service')
    context = {
        'title': 'Services'
    }
    return render(request, 'website/service.html', context)



def booking(request):
    return render(request, 'website/bookings.html')