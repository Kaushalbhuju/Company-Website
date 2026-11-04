from django.db import models
from django.utils.translation import gettext_lazy as _

class CompanyInfo(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company/')
    about = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    class Meta:
        verbose_name = _("Company Information")
        verbose_name_plural = _("Company Information")

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='team/')
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    join_date = models.DateField()

    class Meta:
        verbose_name = _("Team Member")
        verbose_name_plural = _("Team Members")

    def __str__(self):
        return f"{self.name} - {self.position}"

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    content = models.TextField()
    avatar = models.ImageField(upload_to='testimonials/', blank=True)

    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonials")

    def __str__(self):
        return f"{self.client_name} from {self.company}"
    