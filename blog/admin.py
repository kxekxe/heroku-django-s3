from django.contrib import admin
from blog.models import Post, Project
from django.contrib.flatpages.models import FlatPage
from djangoproject import settings


class CollectionAdmin(admin.ModelAdmin):

    class Media:
        js = (
            '%stinymce/tiny_mce.js' % settings.STATIC_URL,
            '%stinymce/tiny_mce_init.js' % settings.STATIC_URL,
            '%sadmin/js/dsbTags.js' % settings.STATIC_URL,
        )


class PostAdmin(CollectionAdmin):
    list_display = ('title', 'created', 'public')
    ordering = ('-created', 'public')

admin.site.register(Post, PostAdmin)
admin.site.register(Project)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CollectionAdmin)
