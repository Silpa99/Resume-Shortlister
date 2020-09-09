from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import *
# Create your views here.
from .models import *
from .forms import ProfileForm, CreateUserForm
#from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + username)
			return redirect('login')
	context = {'form':form}
	return render(request, 'web_app/register.html', context)


@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'web_app/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
	if request.method == 'POST':
		jobid = int(request.POST.get('jobid'))
		jobpost = Job_postings.objects.get(id=jobid)
		print(jobpost)
		jobpost.delete()
	jobpostings = Job_postings.objects.all()
	skills = Skills.objects.all()
	context = {'jobpostings':jobpostings,'skills':skills}
	return render(request ,"web_app/dashboard.html",context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['candidate'])
def userPage(request):
	if request.method == 'POST':
		print(request.POST)
		jobid = int(request.POST.get("jobid"))
		Job_post= Job_postings.objects.get(id=jobid)
		Job_applications.objects.get_or_create(applicant = request.user , post = Job_post)
	jobpostings = Job_postings.objects.all()
	applied_ids = Job_applications.objects.filter(applicant= request.user).values_list("post",flat=True)
	applied_jobs = Job_postings.objects.filter(id__in = applied_ids)
	new_jobs = Job_postings.objects.exclude(id__in = applied_ids)
	print(applied_ids)
	print(new_jobs)
	context = {'jobpostings':jobpostings,'applied_jobs':applied_jobs,'new_jobs':new_jobs}
	return render(request, 'web_app/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['candidate'])
def createprofile(request):
    profile = request.user.profile
    form = ProfileForm(instance = profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,instance=profile)
		#print('Printing POST:', request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'web_app/createprofile.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def skill(request, pk_test):
	skill = Skills.objects.get(id=pk_test)
	context = {'skill':skill}
	return render(request, 'web_app/skill.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_skills(request):
	form = AddSkillsForm()
	if request.method=='POST':
		form = AddSkillsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form': form,}
	return render(request, "web_app/add_skills.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def jobpost(request):
	form = JobPostForm()
	if request.method=='POST':
		form = JobPostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form': form,}
	return render(request, "web_app/jobpost.html", context)
'''
@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def jobapplications(request,pk):
	jobpost = Job_postings.
	context = 
'''