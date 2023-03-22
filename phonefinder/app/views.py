import json
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from sympy import re
from app.forms import UserForm, UserProfileForm
from app.models import Review, Favourite
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.urls import reverse
import json
from urllib.parse import urlencode
import os
from app.filter import filterPhones


def index(request):
    return render(request, 'app/index.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            password = user_form.cleaned_data['password']

            # validata password meets requirements, if not display error message
            # directly from ValidationError
            try:
                validate_password(password)
            except ValidationError as e:
                error_message = f"Password does not meet the requirements due to the following: {''.join(e.messages)}"
                return render(request, 'app/register.html', {'error_message': error_message})

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


def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:

                # log in and render the homepage if user exists and is active
                login(request, user)
                return render(request, 'app/homepage-after-login.html', {})
            else:
                # if user exists but isn't active, display error message
                error_message = "Your account is disabled."
                return render(request, 'app/index.html', {'error_message': error_message})
        else:
            # if user doesn't exist, display error
            error_message = "Incorrect credentials. Please try again or register an account."
            return render(request, 'app/index.html', {'error_message': error_message})
    else:
        return render(request, 'app/index.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('app:index'))


@login_required
def homepageafterlogin(request):
    return render(request, 'app/homepage-after-login.html')


@login_required
def add_favourite(request, phone_id):
    # check if user has 5 favourites already
    user_favourites = Favourite.objects.filter(user=request.user)
    favourites_count = user_favourites.count()

    if favourites_count >= 5:
        oldest = user_favourites.order_by('id').first()
        oldest.delete()

    # Add new favourite
    favourite = Favourite(user=request.user, phone_id=phone_id)
    favourite.save()

    return redirect(reverse('app:favourites'))


@login_required
def submit_review(request):
    if request.method == 'POST':
        # gather data and save review
        rating = request.POST['rating']
        model = request.POST['model']
        title = request.POST['title']
        comments = request.POST['comments']

        review = Review(rating=rating, model=model, title=title,
                        comments=comments, user=request.user.username)
        review.save()

        # redirect to homepage once review is saved
        return redirect(reverse('app:homepageafterlogin'))
    else:
        return HttpResponse('Invalid review')


@login_required
def about(request):
    return render(request, 'app/about.html')


@login_required
def database(request):
    if request.method == "POST":
        phone_json = json.loads(request.body)
        phones = filterPhones(phone_json)
        print(phones)

        # now we filter phones and render the database page
        context = {'phones': phones}
        return JsonResponse(context, safe=False)
    else:
        return render(request, 'app/database.html')


def find(request):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_file_path = os.path.join(BASE_DIR, 'phones.json')
    with open(json_file_path) as json_file:
        phones = json.load(json_file)

    # Create an empty dictionary to hold the possible values for each attribute
        brands = []
        widths = []
        heights = []
        storages = []
        rams = []

        # Loop through each phone and add its attributes to the corresponding list if they're unique
        for phone in phones:
            if phone['brand'] not in brands:
                brands.append(phone['brand'])
            for resolution in phone['resolution'].split(','):
                width, height = resolution.split('x')
                if int(width) not in widths:
                    widths.append(int(width))
                if int(height) not in heights:
                    heights.append(int(height))
            storage = int(float(phone['storage']))
            if storage not in storages:
                storages.append(storage)
            ram = int(float(phone['ram']))
            if ram not in rams:
                rams.append(ram)

        # Construct the context dictionary with the lists of unique attribute values
        context_dict = {
            'brands': brands,
            'widths': sorted(widths),
            'heights': sorted(heights),
            'storages': sorted(storages),
            'rams': sorted(rams),
        }
        json_file.close()

# Render the template with the context dictionary
    return render(request, 'app/find.html', context_dict)


def get_phone(phone_id):
    for phone in phones:
        if phone['id'] == int(phone_id):
            return phone


@login_required
def favourites(request):
    favourite_list = Favourite.objects.filter(user=request.user)
    favourite_phones = [get_phone(favourite.phone_id)
                        for favourite in favourite_list]
    context = {'favourites': favourite_phones}
    return render(request, 'app/favourites.html', context)


@login_required
def review(request):
    # get 5 most recent reviews and pass into context
    recent_reviews = Review.objects.order_by('-pub_date')[:5]

    context_dict = {}
    context_dict['recent_reviews'] = recent_reviews
    context_dict['phones'] = phones
    return render(request, 'app/review.html', context=context_dict)
