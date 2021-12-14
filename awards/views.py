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
# def welcome(request):
#     return render(request, 'base.html')


def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = CreateProfileForm()
    return render(request, 'user/create_profile.html', {"form": form, "title": title})

def email(request):
    current_user = request.user
    email = current_user.email
    name = current_user.username
    send_signup_email(name, email)
    return redirect(create_profile)

@login_required(login_url='/accounts/login/')
def home(request):
    title= "Ann-awwards"
    date = dt.date.today()
    projects = Project.display_all_projects()
    projects_scores = projects.order_by('-average_score')
    highest_score = None
    highest_votes = None
    if len(projects) >= 1:
        highest_score = projects_scores[0]
        votes = Vote.get_project_votes(highest_score.id)
        highest_votes = votes[:3]    
        
    return render(request, "home.html", {"date": date, "title": title, "projects": projects, "highest":highest_score, "votes": highest_votes})

@login_required(login_url='/accounts/login/')
def profile(request, profile_id):
    title = "Ann-awwards"
    try:
        user = User.objects.get(pk = profile_id)
        profile = Profile.objects.get(user = user)
        title = profile.user.username
        projects = Project.get_user_projects(profile.id)
        projects_count = projects.count()
        votes= []
        for project in projects:
            votes.append(project.average_score)
        total_votes = sum(votes)
        average = 0
        if len(projects)> 1:
            average = total_votes / len(projects)
    except Profile.DoesNotExist:
        raise Http404()        
    return render(request, "user/profile.html", {"profile": profile, "projects": projects, "count": projects_count, "votes": total_votes, "average": average, "title": title})

