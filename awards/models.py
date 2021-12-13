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

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete() 

    def edit_bio(self, new_bio):
        self.bio = new_bio
        self.save()

class Project(models.Model):
    name = models.CharField(max_length = 30)
    screenshot = CloudinaryField('Project screenshot')
    description = models.TextField()
    link = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    voters = models.IntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True, null = True)
    average_design = models.FloatField(default=0,)
    average_usability = models.FloatField(default=0)
    average_content = models.FloatField(default=0)
    average_score = models.FloatField(default=0)