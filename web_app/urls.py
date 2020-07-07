from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.login_page,name = "login_page"),
    path('reg/',views.reg_page,name = "reg_page"),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    
    path('recruiter/', views.recruiter, name='recruiter'),
    path('recruiter/addskills/', views.add_skills, name='add_skills'),
    path('recruiter/jobpost/', views.jobpost, name='jobpost'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)