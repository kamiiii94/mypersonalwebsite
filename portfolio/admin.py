from django.contrib import admin
from .models import Project, Technology, ProjectImage
from .models import LearningItem


@admin.register(LearningItem)
class LearningItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)


class ProjectImageInline(admin.TabularInline):  # یا StackedInline
    model = ProjectImage
    extra = 5  # یعنی سه فیلد آپلود تصویر پیش‌فرض


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(ProjectImage)
