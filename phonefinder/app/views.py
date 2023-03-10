from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    return render(request, 'app/index.html')

def register(request):

    return render(request, 'app/register.html')


def homepageafterlogin(request):
    print(request.method)
    print(request.user)
    return render(request, 'app/homepage-after-login.html', {})

def about(request):

    return render(request, 'app/about.html')

def database(request):

    return render(request, 'app/database.html')


def find(request):

    return render(request, 'app/find.html')

def favourites(request):

    return render(request, 'app/favourites.html')

def review(request):
    return render(request, 'app/review.html')