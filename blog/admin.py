from django.contrib import admin
from .models import BlogCategory, BlogTag, BlogPost, BlogComment

class BlogCommentInline(admin.TabularInline):
    model = BlogComment
    extra = 0
    readonly_fields = ('name', 'email', 'content', 'created_at')
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published_at', 'is_published')
    list_filter = ('is_published', 'category', 'tags', 'published_at')
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    inlines = [BlogCommentInline]
    date_hierarchy = 'published_at'
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'category', 'tags', 'excerpt', 'content', 'featured_image')
        }),
        ('Publication', {
            'fields': ('is_published', 'published_at')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
    )

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created_at', 'is_approved')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('name', 'email', 'content', 'post__title')
    list_editable = ('is_approved',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
    approve_comments.short_description = "Approve selected comments"