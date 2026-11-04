from django.contrib import admin
from .models import Service, ServiceFeature, ServiceFAQ

class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 1

class ServiceFAQInline(admin.TabularInline):
    model = ServiceFAQ
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'featured')
    list_filter = ('featured',)
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ServiceFeatureInline, ServiceFAQInline]

@admin.register(ServiceFeature)
class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'service')
    list_filter = ('service',)
    search_fields = ('title', 'description')

@admin.register(ServiceFAQ)
class ServiceFAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'service', 'order')
    list_filter = ('service',)
    search_fields = ('question', 'answer')