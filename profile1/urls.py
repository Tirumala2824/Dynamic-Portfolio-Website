from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import project1,blog1,blogDetail,experience,contact_form



app_name='profile1'
urlpatterns=[
    path('',project1,name='project'),
    path('blog',blog1,name='blog'),
    path('blog/<int:blog_id>/', blogDetail, name='BlogDetail'),
    path('experiences/',experience,name='Experience'),
    path('contact',contact_form,name='contact')
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)