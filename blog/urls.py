
from django.contrib import admin # for importing and using the admin in django
from django.urls import path, include # including the path and include methods
from . import views #importing the views from the same(blog) directory
from django.conf.urls.static import static # importing static for uploading static files  
from django.conf import settings # importing the settings from django.conf package


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home' ),
    path('accounts/', include('accounts.urls')),
    path('student_blog/', include('student_blog.urls')),
] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
