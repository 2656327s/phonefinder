from django.contrib import admin
from app.models import UserProfile
from app.models import PhoneModel


admin.site.register(UserProfile)
# admin.site.register(Review)
admin.site.register(PhoneModel)
