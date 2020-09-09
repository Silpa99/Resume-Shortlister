from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		exclude = ['username']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class AddSkillsForm(ModelForm):
    class Meta:
        model = Skills
        fields = [ 'skill_name', 'jobs']

class JobPostForm(ModelForm):
    class Meta:
        model = Job_postings
        fields = '__all__'

class JobApplyForm(ModelForm):
	class Meta:
		model = Job_postings
		fields = ['id',]


