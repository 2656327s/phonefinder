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

                login(request, user)
                return render(request, 'app/homepage-after-login.html', {})
            else:
                error_message = "Your account is disabled."
                return render(request, 'app/index.html', {'error_message': error_message})
        else:
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
    favourite = Favourite(user=request.user, item=phone_id)
    favourite.save()
    return redirect(reverse('app:favourites'))


@login_required
def favourite_list(request):
    favourites = Favourite.objects.filter(user=request.user)
    context = {'favourites': favourites}
    return render(request, 'app/favourites.html', context)


@login_required
def submit_review(request):
    if request.method == 'POST':
        rating = request.POST['rating']
        model = request.POST['model']
        title = request.POST['title']
        comments = request.POST['comments']

        review = Review(rating=rating, model=model, title=title,
                        comments=comments, user=request.user.username)
        review.save()

        return redirect(reverse('app:homepageafterlogin'))
    else:
        return HttpResponse('Invalid review')


def about(request):
    return render(request, 'app/about.html')


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


# def submit_form(request):
#     if request.method == 'POST':
#         # process the form data as needed
#         data = {
#             'brand': request.POST.get('brand'),
#             'min_year': int(request.POST.get('min_year')),
#             'max_year': int(request.POST.get('max_year')),
#         }
#         # create a JSON response with the desired data
#         response_data = {'success': True, 'data': data}
#         return JsonResponse(response_data)
#     else:
#         # return an error response if the request method is not POST
#         response_data = {'success': False, 'error': 'Invalid request method'}
#         return JsonResponse(response_data, status=400)


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


@login_required
def favourites(request):
    favourites = Favourite.objects.filter(user=request.user)
    context = {'favourites': favourites}
    return render(request, 'app/favourites.html', context)


def review(request):
    return render(request, 'app/review.html')
