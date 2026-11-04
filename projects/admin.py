from django.contrib import admin
from .models import ProjectCategory, Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'category', 'start_date', 'end_date', 'featured')
    list_filter = ('category', 'featured')
    search_fields = ('title', 'client', 'technologies')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption')
    list_filter = ('project',)
    search_fields = ('project__title', 'caption')