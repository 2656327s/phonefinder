from django.urls import path
from app import views
app_name = 'app'

urlpatterns = [
path('', views.index, name='index'),
path('home/', views.homepageafterlogin, name='homepageafterlogin'),
path('register/', views.register, name='register'),
path('about/', views.about, name='about'),
path('database/', views.database, name='database'),
path('find/', views.find, name='find'),
path('favourites/', views.favourites, name='favourites'),
path('database/', views.database, name='database'),
path('review/', views.review, name='review'),
]