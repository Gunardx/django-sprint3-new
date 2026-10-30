from django.contrib import admin
from .models import Post, Category, Location

admin.site.empty_value_display = 'Не задано'


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'slug',
        'is_published',
        'created_at'
    )
    list_editable = (
        'is_published',
        'slug',
        'description'
    )


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at'
    )
    list_editable = (
        'is_published',
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at'
    )
    list_editable = (
        'is_published',
        'category'
    )
    search_fields = ('title', 'text',)
    list_filter = ('category', 'is_published',)


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Location)
