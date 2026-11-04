from django.contrib import admin
from .models import JobCategory, JobType, JobOpening, JobApplication

@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'job_type', 'location', 'is_published', 'published_at')
    list_filter = ('is_published', 'category', 'job_type')
    search_fields = ('title', 'description', 'requirements', 'responsibilities')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'first_name', 'last_name', 'email', 'submitted_at', 'is_reviewed')
    list_filter = ('is_reviewed', 'job', 'submitted_at')
    search_fields = ('first_name', 'last_name', 'email', 'job__title')
    list_editable = ('is_reviewed',)
    date_hierarchy = 'submitted_at'
    readonly_fields = ('submitted_at',)
    