
from django.urls import path, include
from . import views


urlpatterns = [

   path('botanyhome/', views.botanyhome, name='botanyhome'),
   path('commercehome/', views.commercehome, name='commercehome'),
   path('cshome/', views.cshome, name='cshome'),
   path('geographyhome/', views.geographyhome, name='geographyhome'),
   path('historyhome/', views.historyhome, name='historyhome'),
   path('mathhome/', views.mathhome, name='mathhome'),
   path('physicshome/', views.physicshome, name='physicshome'),
   path('yogahome/', views.yogahome, name='yogahome'),
   path('zoologyhome/', views.zoologyhome, name='zoologyhome'),
   path('botanycreate/', views.botanycreate, name='botanycreate'),
   path('commercecreate/', views.commercecreate, name='commercecreate'),
   path('cscreate/', views.cscreate, name='cscreate'),
   path('geographycreate/', views.geographycreate, name='geographycreate'),
   path('historycreate/', views.historycreate, name='historycreate'),
   path('mathcreate/', views.mathcreate, name='mathcreate'),
   path('physicscreate/', views.physicscreate, name='physicscreate'),
   path('yogacreate/', views.yogacreate, name='yogacreate'),
   path('zoologycreate/', views.zoologycreate, name='zoologycreate'),
   path('<int:botany_id>/botanydetail', views.botanydetail, name='botanydetail'),
   path('<int:commerce_id>/commercedetail', views.commercedetail, name='commercedetail'),
   path('<int:cs_id>/csdetail', views.csdetail, name='csdetail'),
   path('<int:geography_id>/geographydetail', views.geographydetail, name='geographydetail'),
   path('<int:history_id>/historydetail', views.historydetail, name='historydetail'),
   path('<int:math_id>/mathdetail', views.mathdetail, name='mathdetail'),
   path('<int:physics_id>/physicsdetail', views.physicsdetail, name='physicsdetail'),
   path('<int:yoga_id>/yogadetail', views.yogadetail, name='yogadetail'),
   path('<int:zoology_id>/zoologydetail', views.zoologydetail, name='zoologydetail'),
   path('<int:botany_id>>/upvote', views.botanyupvote, name='botanyupvote'),
   path('<int:commerce_id>/upvote', views.commerceupvote, name='commerceupvote'),
   path('<int:cs_id>/upvote', views.csupvote, name='csupvote'),
   path('<int:geography_id>/upvote', views.geographyupvote, name='geographyupvote'),
   path('<int:history_id>/upvote', views.historyupvote, name='historyupvote'),
   path('<int:math_id>/upvote', views.mathupvote, name='mathupvote'),
   path('<int:physics_id>/upvote', views.physicsupvote, name='physicsupvote'),
   path('<int:yoga_id>/upvote', views.yogaupvote, name='yogaupvote'),
   path('<int:zoology_id>/upvote', views.zoologyupvote, name='zoologyupvote'),
]
