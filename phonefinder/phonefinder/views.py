from django.shortcuts import render
from app import views

urlpatterns = [
path('', views.index, name='index'),
path('admin/', admin.site.urls),
]