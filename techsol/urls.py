from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    path('projects/', include('projects.urls')),
    path('blog/', include('blog.urls')),
    path('careers/', include('careers.urls')),
    path('contact/', include('contacts.urls')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]