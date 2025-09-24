from django.shortcuts import render, get_object_or_404
from blog.models import Post

def post_detail(request, slug=None):
    if slug:
        post = get_object_or_404(Post, slug=slug)
    else:
        post = Post.objects.order_by('?').first()  # post aleatório

    sidebar_posts = Post.objects.exclude(pk=post.pk).order_by('?')[:6]

    return render(request, 'noticias.html', {
        'post': post,
        'sidebar_posts': sidebar_posts
    })
