from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.urls import reverse


def index(request):

    return render(request, 'app/index.html')

def register(request):
   
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'app/register.html',
                  context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})



def homepageafterlogin(request):
    
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:

                login(request, user)
                return redirect(reverse('phonefinder:index'))
            else:
                return HttpResponse("Your PhoneFinder account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
         
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