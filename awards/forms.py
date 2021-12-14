from .models import Project, Profile, Vote
from django.forms import ModelForm
from django import forms

class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class AddProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['profile', 'post_date', 'voters', 'design_score','usability_score','content_score','average_design','average_usability','average_content','average_score']

class RateProjectForm(ModelForm):
    class Meta:
        model = Vote
        exclude = ['post_date', 'voter', 'project'] 
