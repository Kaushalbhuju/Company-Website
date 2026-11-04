from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = _("Project Category")
        verbose_name_plural = _("Project Categories")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True, blank=True)
    client = models.CharField(max_length=100)
    short_description = models.TextField()
    challenge = models.TextField()
    solution = models.TextField()
    result = models.TextField()
    featured_image = models.ImageField(upload_to='projects/')
    start_date = models.DateField()
    end_date = models.DateField()
    website = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    technologies = models.CharField(max_length=200, help_text="Comma separated list of technologies used")

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
        ordering = ['-end_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def tech_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/')
    caption = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = _("Project Image")
        verbose_name_plural = _("Project Images")

    def __str__(self):
        return f"Image for {self.project.title}"