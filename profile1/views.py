from django.shortcuts import render,get_object_or_404
from .models import project,blog,Experience

# Create your views here.
def project1(request):
    projects=project.objects.all()
    return render(request,'portfolio/index.html',{"projects":projects})

def blog1(request):
    blogs=blog.objects.order_by('-date')[:10]
    return render(request,'portfolio/blog.html',{'blogs':blogs})

def blogDetail(request,blog_id):
    blog3=get_object_or_404(blog,pk=blog_id)
    return render(request,'portfolio/blogDetail.html',{'blogs':blog3})

def experience(request):
    experiences=Experience.objects.all()
    return render(request,'portfolio/Experience.html',{'experiences':experiences})
