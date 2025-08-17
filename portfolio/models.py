from django.db import models
from django.shortcuts import render, get_object_or_404

# Create your models here.


class Technology(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='technology_images/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField(blank=True)
    technologies = models.CharField(max_length=200, blank=True)
    technology = models.ForeignKey(
        Technology,
        on_delete=models.CASCADE,
        related_name='projects',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"


class LearningItem(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان")
    description = models.TextField(blank=True, verbose_name="توضیح")
    image = models.ImageField(
        upload_to='learning_items/', blank=True, null=True, verbose_name="تصویر")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "موارد در حال یادگیری"
        verbose_name_plural = "موارد در حال یادگیری"
