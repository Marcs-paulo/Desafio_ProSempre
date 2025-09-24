from django.http import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post

def post_list(request):
    # 1️⃣ Receber filtros e ordenação via GET
    selected_tags = request.GET.getlist('tag')  # lista de tags selecionadas
    selected_sort = request.GET.get('sort', 'recent')

    # 2️⃣ Queryset inicial
    posts = Post.objects.all()

    # 3️⃣ Aplicar filtro por tags
    if selected_tags:
        posts = posts.filter(tag__in=selected_tags)

    # 4️⃣ Aplicar ordenação
    if selected_sort == 'recent':
        posts = posts.order_by('-date')
    elif selected_sort == 'old':
        posts = posts.order_by('date')
    elif selected_sort == 'popular':
        # Exemplo: se você tiver um campo 'popularity' no Post
        posts = posts.order_by('-popularity')

    # 5️⃣ Paginação
    paginator = Paginator(posts, 5)  # 5 posts por página
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # 6️⃣ Posts em destaque (aleatórios)
    featured_posts = Post.objects.all().order_by('?')[:3]

    # 7️⃣ Renderizar template
    return render(request, "blog.html", {
        "page_obj": page_obj,
        "featured_posts": featured_posts,
        "selected_tags": selected_tags,
        "selected_sort": selected_sort,
    })


# Rota para retornar 3 posts aleatórios em JSON
def featured_posts_api(request):
    posts = Post.objects.all().order_by('?')[:3]
    data = []
    for post in posts:
        data.append({
            "image": post.image.url,
            "title": post.title,
            "content": post.content[:200],  # limitar texto
            "tag": post.get_tag_display(),
            "date": post.date.strftime("%d/%m/%Y"),
            "author": post.author,
            "link": f"/noticias/{post.slug}"
        })
    return JsonResponse({"posts": data})
