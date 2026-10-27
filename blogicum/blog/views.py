from django.shortcuts import render
from django.http import Http404


def index(request):
    template_name = 'blog/index.html'
    context = {'posts': posts}
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    try:
        post = posts[id]
    except IndexError:
        raise Http404('Пост не найден')
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template_name, context)
