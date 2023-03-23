from django.contrib import admin
from app.models import UserProfile, Review, Favourite
from django.contrib.auth.models import User


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'


class FavouriteInline(admin.TabularInline):
    model = Favourite
    extra = 0


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


class CustomUserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline, FavouriteInline, ReviewInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Review)

