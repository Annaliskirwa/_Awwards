from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = CloudinaryField('Profile Picture')
    bio =  models.TextField()
    location = models.CharField(max_length = 40)
    email = models.EmailField()
    link = models.URLField()