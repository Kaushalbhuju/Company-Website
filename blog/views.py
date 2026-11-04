from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import BlogPost, BlogCategory, BlogTag

def blog_list(request):
    posts = BlogPost.objects.filter(is_published=True).order_by('-published_at')
    categories = BlogCategory.objects.all()
    tags = BlogTag.objects.all()
    
    # Filter by category if specified
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(BlogCategory, slug=category_slug)
        posts = posts.filter(category=category)
    else:
        category = None
    
    # Filter by tag if specified
    tag_slug = request.GET.get('tag')
    if tag_slug:
        tag = get_object_or_404(BlogTag, slug=tag_slug)
        posts = posts.filter(tags=tag)
    else:
        tag = None
    
    # Pagination
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blog/list.html', {
        'page_obj': page_obj,
        'categories': categories,
        'tags': tags,
        'selected_category': category,
        'selected_tag': tag,
    })

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    related_posts = BlogPost.objects.filter(
        is_published=True
    ).exclude(id=post.id)[:3]
    
    # Handle comments submission
    if request.method == 'POST':
        # Comment form handling would go here
        pass
    
    return render(request, 'blog/detail.html', {
        'post': post,
        'related_posts': related_posts,
    })