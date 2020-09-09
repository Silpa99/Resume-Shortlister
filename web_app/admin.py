from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Profile)
admin.site.register(Job_postings)
admin.site.register(Skills)
admin.site.register(Userskills)
admin.site.register(Job_applications)