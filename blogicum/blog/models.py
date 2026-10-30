from django.db import models
from django.contrib.auth import get_user_model
from core.models import BaseModel

MAX_STR_LEN = 50
MAX_FIELD_LEN = 256

User = get_user_model()


class Post(BaseModel):
    """
    Публикация в блоге.

    Содержит заголовок, текст, дату публикации, автора,
    местоположение и категорию. По умолчанию сортируется
    по убыванию даты публикации.
    """

    title = models.CharField(
        max_length=MAX_FIELD_LEN, verbose_name='Заголовок'
    )
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — '
        'можно делать отложенные публикации.'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
        related_name='user_posts'
    )
    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Местоположение',
        related_name='location_posts'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='category_posts',
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title[:MAX_STR_LEN]


class Category(BaseModel):
    """
    Категория публикаций.

    Имеет заголовок, описание и уникальный slug,
    который используется в URL страницы категории.
    """

    title = models.CharField(
        max_length=MAX_FIELD_LEN, verbose_name='Заголовок'
    )
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        unique=True, verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; разрешены символы латиницы,'
        'цифры, дефис и подчёркивание.'
    )

    class Meta(BaseModel.Meta):
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title[:MAX_STR_LEN]


class Location(BaseModel):
    """
    Местоположение, к которому может быть привязана публикация.

    Содержит только название места.
    """

    name = models.CharField(
        max_length=MAX_FIELD_LEN, verbose_name='Название места'
    )

    class Meta(BaseModel.Meta):
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name[:MAX_STR_LEN]
