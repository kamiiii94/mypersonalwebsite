from django.shortcuts import render, get_object_or_404
from .models import Project, Technology
from .forms import ContactForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import LearningItem


def home(request):
    technologies = Technology.objects.all()
    learning_items = LearningItem.objects.all()
    return render(request, 'portfolio/home.html', {
        'technologies': technologies,
        'learning_items': learning_items
    })


def technology_projects(request, tech_id):
    technology = get_object_or_404(Technology, id=tech_id)
    projects = Project.objects.filter(technology=technology)
    return render(request, 'portfolio/technology_projects.html', {
        'technology': technology,
        'projects': projects
    })


def about(request):
    # صفحه درباره من
    return render(request, 'portfolio/about.html')


def projects(request):
    # صفحه پروژه‌ها - لیست همه پروژه‌ها
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})


def contact(request):
    return render(request, 'portfolio/contact.html')


def interests(request):
    # صفحه علاقه‌مندی‌ها - اگر مدل خاص نداری، داده استاتیک بفرست
    interests_list = [
        "تحلیل داده", "GIS", "برنامه‌نویسی وب", "هوش مصنوعی", "یادگیری ماشین"
    ]
    return render(request, 'portfolio/interests.html', {'interests': interests_list})


def education(request):
    # صفحه تحصیلات - اطلاعات تحصیلی استاتیک یا از مدل
    education_info = {
        "degree": "کارشناسی ارشد مهندسی نرم‌افزار",
        "university": "خواجه نصیرالدین طوسی",
        "year": "۱۴۰۱ - ۱۴۰۳"
    }
    return render(request, 'portfolio/education.html', {'education': education_info})


# you can comment multiple line with alt + shift and A
#
""" def technology_list(request):
    technologies = Technology.objects.all()
    return render(request, 'portfolio/technology_list.html', {'technologies': technologies})


    # ویو جزئیات تکنولوژی برای نمایش پروژه‌های مرتبط
def technology_detail(request, pk):
    tech = get_object_or_404(Technology, pk=pk)
    projects = tech.project_set.all()  # فرض بر این که پروژه‌ها به تکنولوژی‌ها FK دارند
    return render(request, 'portfolio/technology_detail.html', {
        'technology': tech,
        'projects': projects
    }) """
