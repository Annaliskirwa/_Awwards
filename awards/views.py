import datetime as dt
import statistics

from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import AddProjectForm, RateProjectForm, CreateProfileForm
from .email import send_signup_email
from django.contrib.auth.models import User
from .models import Profile, Project, Vote
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.
def welcome(request):
    return render(request, 'base.html')

