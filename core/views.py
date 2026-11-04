from django.shortcuts import render
from core.models import CompanyInfo, TeamMember, Testimonial
from services.models import Service
from projects.models import Project

def home(request):
    company = CompanyInfo.objects.first()
    services = Service.objects.filter(featured=True)[:6]
    featured_projects = Project.objects.filter(featured=True)[:4]
    testimonials = Testimonial.objects.all()[:5]
    team_members = TeamMember.objects.all()[:4]
    
    context = {
        'company': company,
        'services': services,
        'featured_projects': featured_projects,
        'testimonials': testimonials,
        'team_members': team_members,
    }
    return render(request, 'core/home.html', context)

def about(request):
    company = CompanyInfo.objects.first()
    team_members = TeamMember.objects.all()
    
    context = {
        'company': company,
        'team_members': team_members,
    }
    return render(request, 'core/about.html', context)