from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'website/index.html')

def aboutUs(request):
    return render(request, 'website/about-us.html')

def blog(request):
    return render(request, 'website/blog.html')

def blogDetail(request):
    return render(request, 'website/blogDetail.html')

def contact(request):
    return render(request, 'website/contact-us.html')

def ourWork(request):
    return render(request, 'website/ourWork.html')

def service(request):
    return render(request, 'website/service.html')