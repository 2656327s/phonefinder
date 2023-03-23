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
    path('all-phones/individual/<slug:manufacturer_slug>/<slug:model_slug>', views.show_individual,
         name='show_individual'),
    path('favourites/', views.favourites, name='favourites'),
    path('favorites/add/<int:phone_id>/',
         views.add_favourite, name='add_favourite'),
    path('all-phones/', views.database, name='database'),
    path('review/', views.review, name='review'),
    path('review/search/', views.search, name='search'),

    path('submit_review/', views.submit_review, name='submit_review'),
]
