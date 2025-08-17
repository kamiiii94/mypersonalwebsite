from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # صفحه اصلی

    path('about/', views.about, name='about'),  # درباره من
    path('projects/', views.projects, name='projects'),  # پروژه‌ها
    path('contact/', views.contact, name='contact'),  # تماس
    path('interests/', views.interests, name='interests'),  # علاقه‌مندی‌ها
    path('education/', views.education, name='education'),  # تحصیلات

    # مسیر پروژه‌های تکنولوژی (اگر لازم باشه نگه داریم)
    path('technology/<int:tech_id>/',
         views.technology_projects, name='technology_projects'),
]


""" from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),  # صفحه اصلی
    path('technology/<int:tech_id>/', views.technology_projects, name='technology_projects'),
    
]

 """
#    path('technologies/', views.technology_list, name='technology_list'),
#    path('technologies/<int:pk>/', views.technology_detail, name='technology_detail'),
#    path('technology/<int:tech_id>/', views.technology_projects, name='technology_projects'),
