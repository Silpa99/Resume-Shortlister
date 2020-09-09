from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}/{1}'.format(instance.username, filename)
# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE,null = True)
    name = models.CharField(max_length=30,null = True)
    phoneno = models.IntegerField(null = True)
    dob = models.DateField(null = True)
    upload_your_resume = models.FileField(upload_to = user_directory_path,null = True)
    def __str__(self):
        return self.name
    
class Job_postings(models.Model):
    company = models.CharField(max_length=30,null = True)
    title = models.CharField(max_length=30,null=True)
    description = models.CharField(max_length=100,null = True)
    job_address = models.CharField(max_length=30, null = True)
    def __str__(self):
        return self.title

class Skills(models.Model):
    skill_name = models.CharField(max_length = 40)
    jobs = models.ManyToManyField(Job_postings)
    def __str__(self):
        return self.skill_name

class Userskills(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    u_skill = models.ForeignKey(Skills, on_delete = models.CASCADE)
    def __str__(self):
        return self.u_skill


class Job_applications(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Job_postings, on_delete=models.CASCADE, related_name='applicants')
    is_shortlisted = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    evaluated_score = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.applicant.username}-{self.post.title}'