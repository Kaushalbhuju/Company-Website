from django.contrib import admin
from .models import CompanyInfo, TeamMember, Testimonial

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'join_date')
    search_fields = ('name', 'position')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'position')
    search_fields = ('client_name', 'company')