from django.shortcuts import render,get_object_or_404,redirect
from django.core.mail import send_mail
from .models import project,blog,Experience
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ContactForm

# Create your views here.
def project1(request):
    projects=project.objects.all()
    
    return render(request,'portfolio/index.html',{"projects":projects})

def blog1(request):
    blogs_list=blog.objects.all()
    blogs_per_page=10
    paginator=Paginator(blogs_list,blogs_per_page)
    
    page=request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        blogs = paginator.page(paginator.num_pages)
    
    
    return render(request,'portfolio/blog.html',{'blogs':blogs})


def blogDetail(request,blog_id):
    blog3=get_object_or_404(blog,pk=blog_id)
    return render(request,'portfolio/blogDetail.html',{'blogs':blog3})

def experience(request):
    experiences=Experience.objects.all()
    return render(request,'portfolio/Experience.html',{'experiences':experiences})




def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            company = form.cleaned_data['company']
            message = form.cleaned_data['message']
            subject = f'Message from {name}'
            body = f'Name: {name}\nEmail: {email}\nCompany: {company}\nMessage: {message}'
            send_mail(subject, body, email, ['ptvdprasad121@gmail.com'])
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contactForm.html', {'form': form})
