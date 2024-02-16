from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import project1,blog1

urlpatterns=[
    path('',project1,name='project'),
    path('blog',blog1,name='blog')
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)