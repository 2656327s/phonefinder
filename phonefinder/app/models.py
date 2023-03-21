from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_id = models.CharField(max_length=256)


class Review(models.Model):
    rating = models.IntegerField()
    model = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    comments = models.TextField()
    user = models.CharField(max_length=100, default="")
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title
