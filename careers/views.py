from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import JobOpening, JobCategory, JobType
from .forms import JobApplicationForm

def job_list(request):
    jobs = JobOpening.objects.filter(is_published=True).order_by('-published_at')
    categories = JobCategory.objects.all()
    job_types = JobType.objects.all()
    
    # Filter by category if specified
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(JobCategory, slug=category_slug)
        jobs = jobs.filter(category=category)
    else:
        category = None
    
    # Filter by job type if specified
    type_slug = request.GET.get('type')
    if type_slug:
        job_type = get_object_or_404(JobType, slug=type_slug)
        jobs = jobs.filter(job_type=job_type)
    else:
        job_type = None
    
    return render(request, 'careers/list.html', {
        'jobs': jobs,
        'categories': categories,
        'job_types': job_types,
        'selected_category': category,
        'selected_type': job_type,
    })

def job_detail(request, slug):
    job = get_object_or_404(JobOpening, slug=slug, is_published=True)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('careers:detail', slug=job.slug)
    else:
        form = JobApplicationForm()
    
    return render(request, 'careers/detail.html', {
        'job': job,
        'form': form,
    })