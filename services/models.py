from django.db import models
from django.utils.translation import gettext_lazy as _

class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    short_description = models.TextField()
    full_description = models.TextField()
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")
        ordering = ['order']

    def __str__(self):
        return self.title

class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, related_name='features', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = _("Service Feature")
        verbose_name_plural = _("Service Features")

    def __str__(self):
        return f"{self.title} for {self.service.title}"

class ServiceFAQ(models.Model):
    service = models.ForeignKey(Service, related_name='faqs', on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = _("Service FAQ")
        verbose_name_plural = _("Service FAQs")
        ordering = ['order']

    def __str__(self):
        return f"{self.question} - {self.service.title}"