from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = _("Blog Category")
        verbose_name_plural = _("Blog Categories")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class BlogTag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = _("Blog Tag")
        verbose_name_plural = _("Blog Tags")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(BlogTag, blank=True)
    excerpt = models.TextField()
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=300, blank=True)

    class Meta:
        verbose_name = _("Blog Post")
        verbose_name_plural = _("Blog Posts")
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Blog Comment")
        verbose_name_plural = _("Blog Comments")
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"