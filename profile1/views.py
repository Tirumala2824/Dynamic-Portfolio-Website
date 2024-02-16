from django.shortcuts import render
from .models import project,blog

# Create your views here.
def project1(request):
    projects=project.objects.all()
    return render(request,'portfolio/index.html',{"projects":projects})

def blog1(request):
    blogs=blog.objects.all()
    return render(request,'portfolio/blog.html',{'blogs':blogs})