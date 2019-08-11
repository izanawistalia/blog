from django.urls import path, include
from . import views # importing views from the same(accounts) directory 

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
