import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phonefinder.settings')

import django

django.setup()

from django.contrib.auth.models import User
from app.models import Favourite, Review


def populate():
    
    Users_test = [
        {'user_name': 'Abdulrahman', 'email': '', 'password': 'abs11223344?'},
        {'user_name': 'James', 'email': 'James35@gmail.com', 'password': 'james112233'},
        {'user_name': 'Ahmed', 'email': 'Ahmed11uk@gmail.com', 'password': 'Ahmed2233'},
    ]
    
    for i in Users_test:
        user = User.objects.create_user(username=i['user_name'], email=i['email'], password=i['password'])
    
    reviews = [
            {'rating': 5, 'model': 'Samsung Galaxy S20', 'title': 'Amazing phone', 'comments': 'I am loving this phone!'},
            {'rating': 4, 'model': 'iPhone X', 'title': 'Great phone', 'comments': 'I love this phone!'},
            {'rating': 2, 'model': 'Google Pixel 5', 'title': 'Okay phone', 'comments': 'This phone is just okay.'},
    ]
    
    for r in reviews:
            Review.objects.create(rating=r['rating'], model=r['model'], title=r['title'], comments=r['comments'], user=user)
    
    favourites = [
            {'phone_id': '251'},
            {'phone_id': '350'},
            {'phone_id': '91'},
    ]
    
    for f in favourites:
            Favourite.objects.create(user=user, phone_id=f['phone_id'])
    


if _name_ == '_main_':
    print('Starting PhoneFinder population script...')
    populate()