from django.contrib import admin
from app.models import UserProfile, Review, Favourite


admin.site.register(UserProfile)
admin.site.register(Review)
admin.site.register(Favourite)
