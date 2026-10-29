from django.shortcuts import get_object_or_404, render
from .models import Post, Category
from django.utils import timezone


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte = timezone.now()
    )
    context = {'post_list': post_list,}
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte = timezone.now(),
            ),
            id=id
    )
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte = timezone.now(),
        category__slug=category_slug
        )
    category = get_object_or_404(
        Category.objects.values(
            'title', 'description'
            ).filter(is_published=True),
            slug=category_slug
            )
    context = {
        'post_list': post_list,
        'category': category
        }
    return render(request, template_name, context)