from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

class JobCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = _("Job Category")
        verbose_name_plural = _("Job Categories")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class JobType(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = _("Job Type")
        verbose_name_plural = _("Job Types")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class JobOpening(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True)
    job_type = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    responsibilities = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = _("Job Opening")
        verbose_name_plural = _("Job Openings")
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def is_active(self):
        if self.application_deadline:
            return self.is_published and timezone.now().date() <= self.application_deadline
        return self.is_published

class JobApplication(models.Model):
    job = models.ForeignKey(JobOpening, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_reviewed = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Job Application")
        verbose_name_plural = _("Job Applications")
        ordering = ['-submitted_at']

    def __str__(self):
        return f"Application for {self.job.title} by {self.first_name} {self.last_name}"