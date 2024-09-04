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
    teams = Team.objects.all()
    if request.method == 'POST':
        email = request.POST['email']
        
        newsletter = NewsLetter(email=email)
        newsletter.save()
        return redirect('aboutUs')
    
    context = {
        'teams': teams,
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
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        company_name = request.POST['company_name']
        project_type = request.POST['project_type']
        project_description = request.POST['project_description']
        existing_website = request.POST['existing_website']
        desired_deadline = request.POST['desired_deadline']
        estimated_budget = request.POST['estimated_budget']
        preferred_start_date = request.POST['preferred_start_date']
        additional_notes = request.POST['additional_notes']
        
        bookings = Booking(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, company_name=company_name, project_type=project_type, project_description=project_description, existing_website=existing_website, desired_deadline=desired_deadline, estimated_budget=estimated_budget, preferred_start_date=preferred_start_date, additional_notes=additional_notes)
        bookings.save()
        return redirect('booking')
    return render(request, 'website/bookings.html')