from django.db import models
from django.utils.translation import gettext_lazy as _

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    service = models.CharField(max_length=100, blank=True)
    project = models.CharField(max_length=100, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Contact Submission")
        verbose_name_plural = _("Contact Submissions")
        ordering = ['-submitted_at']

    def __str__(self):
        return f"Contact from {self.name} - {self.subject}"