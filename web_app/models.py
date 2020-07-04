from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    phoneno = models.IntegerField()
    dob = models.DateField()
    #resume = models.FileField(upload_to = user_directory_path)
    
class Job_postings(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

class Skills(models.Model):
    skill_name = models.CharField(max_length = 40)
    jobs = models.ManyToManyField(Job_postings)

class Userskills(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    u_skill = models.ForeignKey(Skills, on_delete = models.CASCADE)


class Job_applications(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Job_postings, on_delete=models.CASCADE)
    is_shortlisted = models.CharField(max_length=30)
    is_approved = models.CharField(max_length=30)