from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user_ptr.id, filename)

class Profile(User):
    #userid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    phoneno = models.IntegerField()
    dob = models.DateField()
    upload_your_resume = models.FileField(upload_to = user_directory_path)
    def __str__(self):
        return self.name
    
class Job_postings(models.Model):
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    job_address = models.CharField(max_length=30)
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
        return self.user


class Job_applications(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Job_postings, on_delete=models.CASCADE)
    is_shortlisted = models.CharField(max_length=30)
    is_approved = models.CharField(max_length=30)
    def __str__(self):
        return self.applicant