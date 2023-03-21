from django.urls import path
from app import views
app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('home/', views.homepageafterlogin, name='homepageafterlogin'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('database/', views.database, name='database'),
    path('find/', views.find, name='find'),
    path('favourites/', views.favourites, name='favourites'),
    path('favorites/add/<int:phone_id>/',
         views.add_favourite, name='add_favorite'),
    path('database/', views.database, name='database'),
    path('review/', views.review, name='review'),
    path('submit_review/', views.submit_review, name='submit_review'),
]
