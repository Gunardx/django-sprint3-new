from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Post, Category

MAX_POSTS = 5


def get_published_posts():
    """Возвращает отфильтрованный QuerySet"""
    return Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    """
    Главная страница с лентой последних публикаций.

    Выводит не более MAX_POSTS опубликованных постов,
    у которых категория также опубликована,
    а дата публикации не находится в будущем времени.
    """
    template_name = 'blog/index.html'
    post_list = get_published_posts().select_related(
        'author', 'category', 'location',
    )[:MAX_POSTS]

    context = {'post_list': post_list, }
    return render(request, template_name, context)


def post_detail(request, id):
    """
    Страница отдельной публикации.

    Возвращает страницу поста с указанным id,
    если он опубликован, его категория опубликована,
    а дата публикации не в будущем времени.
    В ином случае возвращает 404.
    """
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        get_published_posts(),
        id=id,
    )
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    """
    Страница публикаций выбранной категории.

    Находит категорию по slug. Если категория не найдена
    или не опубликована — возвращает 404.
    Выводит все опубликованные посты этой категории,
    у которых дата публикации не в будущем времени.
    """
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = category.posts.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
    )
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template_name, context)
