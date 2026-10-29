from django.shortcuts import get_object_or_404, render
from .models import Post, Category
from django.utils import timezone

MAX_POSTS = 5

def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte = timezone.now()
    ).[:MAX_POSTS]

    context = {'post_list': post_list,}
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        id=id,
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now(),
        )
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = Post.objects.filter(
        is_published=True,
        category=category,
        pub_date__lte=timezone.now(),
    )
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template_name, context)