from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.user.username


class Review(models.Model):
    rating = models.IntegerField()
    model = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    comments = models.TextField()

    def __str__(self):
        return self.title
