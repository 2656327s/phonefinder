from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


# class Favourite(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     phone_id = models.CharField(max_length=256)


# class Review(models.Model):
#     rating = models.IntegerField()
#     model = models.CharField(max_length=100)
#     title = models.CharField(max_length=100)
#     comments = models.TextField()
#     user = models.CharField(max_length=100, default="")

#     def __str__(self):
#         return self.title


class PhoneModel(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=128)
    brand = models.CharField(max_length=128)
    releaseYear = models.IntegerField()
    storage = models.IntegerField()
    resolution = models.CharField(max_length=32)
    ram = models.IntegerField()
    picture = models.CharField(max_length=512)
    isFavourite = models.BooleanField(default=False)

    class Meta:
        db_table = "phones"
