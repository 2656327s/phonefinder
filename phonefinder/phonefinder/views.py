from django.shortcuts import render
from app import views
import path

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
