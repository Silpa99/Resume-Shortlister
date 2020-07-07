from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate
from .models import Profile
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def login_page(request):
    form = UserLoginForm()
    if request.method == 'POST':
       if not request.user.is_authenticated:
           return HttpResponseRedirect(reverse('login_page'))
       else:
           return HttpResponseRedirect(reverse('dashboard'))
    return render(request, 'web_app/login_page.html',{'form':form})

def reg_page(request):
    form = UserRegisterForm(request.POST, request.FILES)
    if request.method=='POST':
        next = request.GET.get('next')
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            #new_user = authenticate(username=user.username, password=password)
            #login(request, new_user)
            return redirect('login_page')

    context = {
        'form': form,
    }
    return render(request, "web_app/reg_page.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required()
def dashboard(request):
    return render(request, "web_app/dashboard.html")




def add_skills(request):
    form = AddSkillsForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            form = AddSkillsForm()
            return redirect('recruiter')

    context = {
        'form': form,
    }
    return render(request, "web_app/add_skills.html", context)

def recruiter(request):
    form = RecruiterForm(request.POST)

    context = {
        'form': form,
    }
    return render(request, "web_app/recruiter.html", context)

def jobpost(request):
    form = JobPostForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            form = AddSkillsForm()
            return redirect('recruiter')

    context = {
        'form': form,
    }
    return render(request, "web_app/jobpost.html", context)


