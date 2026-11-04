from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import ContactSubmission

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contacts:contact')
    else:
        initial = {}
        if 'service' in request.GET:
            initial['service'] = request.GET.get('service')
        if 'project' in request.GET:
            initial['project'] = request.GET.get('project')
        form = ContactForm(initial=initial)
    
    return render(request, 'contacts/contact.html', {'form': form})