from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectCategory

def project_list(request):
    projects = Project.objects.all().order_by('-end_date')
    categories = ProjectCategory.objects.all()
    
    # Filter by category if specified
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(ProjectCategory, slug=category_slug)
        projects = projects.filter(category=category)
    else:
        category = None
    
    return render(request, 'projects/list.html', {
        'projects': projects,
        'categories': categories,
        'selected_category': category,
    })

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.filter(category=project.category).exclude(id=project.id)[:3]
    return render(request, 'projects/detail.html', {
        'project': project,
        'related_projects': related_projects,
    })