from django.contrib import admin
from api.models import Question, Option


admin.site.register(Question)
admin.site.register(Option)