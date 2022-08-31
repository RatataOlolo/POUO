from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):  # posts/news on page
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, verbose_name='Головне зображення новини')
    text = models.TextField(max_length=15255, blank=True, verbose_name='Текст')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата останніх змін')
    is_published = models.BooleanField(default=True, verbose_name='Опубліковано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, default=None, verbose_name='Категорія')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Статті'
        verbose_name_plural = 'Статті'
        ordering = ['time_create', 'title']


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.CharField(max_length=255, blank=True, verbose_name='Опис')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата останніх змін')
    is_published = models.BooleanField(default=True, verbose_name='Опубліковано')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категорії'
        verbose_name_plural = 'Категорії'
        ordering = ['time_create', 'title']


class PostPhotos(models.Model):
    photo = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата останніх змін')
    is_published = models.BooleanField(default=True, verbose_name='Опубліковано')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, default=None, verbose_name='Новина')

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = 'Фото до статті'
        verbose_name_plural = 'Фото до статей'
        ordering = ['time_create', 'time_update', 'is_published', 'post']
