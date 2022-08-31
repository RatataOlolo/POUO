from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostPhotosInline(admin.StackedInline):
    model = PostPhotos
    extra = 1
    readonly_fields = ('img_show_in_post',)

    def img_show_in_post(self, obj):
        if obj.photo:
            return mark_safe(f"<img src = {obj.photo.url} width='60'>")
        return None

    img_show_in_post.short_description = 'Зображення'


class PostAdmin(admin.ModelAdmin):
    inlines = [PostPhotosInline]
    list_display = ('id', 'title', 'time_create', 'time_update', 'img_show', 'is_published', 'cat')
    readonly_fields = ('img_show_in_post',)
    list_display_links = ('id', 'title')
    form = PostAdminForm
    search_fields = ('title', 'time_create')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_update', 'time_create')
    prepopulated_fields = {'slug': ('title',)}

    def img_show(self, obj):
        if obj.photo:
            return mark_safe(f"<img src = {obj.photo.url} width='60'>")
        return None

    def img_show_in_post(self, obj):
        if obj.photo:
            return mark_safe(f"<img src = {obj.photo.url} width='60'>")
        return None

    img_show_in_post.short_description = 'Зображення'

    img_show.__name__ = 'IMG'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'time_update', 'description', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'time_create')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_update', 'time_create')
    prepopulated_fields = {'slug': ('title',)}


class PostPhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'img_show', 'time_create', 'time_update', 'is_published', 'post')
    readonly_fields = ('img_show_in_post',)
    list_display_links = ('id', 'img_show')
    search_fields = ('time_create', 'time_update', 'post')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_update', 'time_create', 'post')

    def img_show(self, obj):
        if obj.photo:
            return mark_safe("<img src = '{}' width=60 />".format(obj.photo.url))
        return None

    def img_show_in_post(self, obj):
        if obj.photo:
            return mark_safe(f"<img src = {obj.photo.url} width='60'>")
        return None

    img_show.__name__ = 'IMG'
    img_show_in_post.short_description = 'Зображення'


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PostPhotos, PostPhotosAdmin)
