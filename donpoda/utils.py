from .models import *
from django.db.models import Count

class DataMixin:
    paginate_by = 12

    def get_user_context(self, **kwargs):
        context = kwargs
        photos = PostPhotos.objects.annotate(Count('post'))
        cats = Category.objects.annotate(Count('post')).order_by('-time_create')
        newsposts = Post.objects.filter(is_published=True).order_by('-time_create')[0:5]
        catposts = Post.objects.filter(is_published=True).order_by('-time_create')[0:10]

        context['photos'] = photos
        context['cats'] = cats
        context['newsposts'] = newsposts
        context['catposts'] = catposts

        return context

def get_filename(filename):
    return filename.upper()