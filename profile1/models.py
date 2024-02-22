from django.db import models

# Create your models here.
class  project(models.Model):
    title=models.CharField(max_length=100)
    projectType=models.CharField(choices={
        "Personal Project":'Personal Project',
        'Internship Project':'Internship',
        'Academic Project':'Academic Projects',
        'Freelancing Project':'Freelance Project',
        'Case Studies':'Case Study'
    },default='Personal Project')
    aim=models.TextField(max_length=200,null=True)
    startDate=models.DateField()
    endDate=models.DateField()
    image=models.ImageField(upload_to='images/')
    project_url=models.URLField(null=True)
    Description=models.TextField(max_length=500)
    
    def __str__(self):
        return self.title
    
    

class blog(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateField()
    description=models.TextField(max_length=500)
    
    
    def __str__(self):
        return self.title
    
    
class Experience(models.Model):
    companyTitle=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    companyImage=models.ImageField(upload_to='images/',null=True)
    startDate=models.DateField()
    endDate=models.DateField()
    projects=models.ForeignKey(project,on_delete=models.CASCADE,null=True,blank=True)
    jobType=models.CharField(choices={
        'Internship':'Intern ship',
        'Full Time':'FUll Time',
        'Part Time':'Part Time',
        'Contract':'Contract',
        'Freelance':'Freelance',
    },default='Full Time')
    jobDescription=models.TextField(max_length=1000)
    
    def __str__(self):
        return self.companyTitle + " " + self.role
    
    
    