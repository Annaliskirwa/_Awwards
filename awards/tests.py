from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Project, Vote

# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        self.Annalis = User(username = "Annalis", email = "annaliskirwa@gmail.com",password = "Ann")
        self.profile = Profile(user= self.Annalis, profile_pic='mepng',bio='bio', location='Nairobi, Kenya', email='annaliskirwa@gmail', link='www.ann.com')
        self.Annalis.save()
        self.profile.save_profile()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.lorna, User))
        self.assertTrue(isinstance(self.profile, Profile))

    def test_edit_bio(self):
        self.profile.edit_bio('I am a software engineer')
        self.assertEqual(self.profile.bio, 'I am a software engineer')