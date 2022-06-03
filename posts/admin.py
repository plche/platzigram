"""Post admin classes."""

# Django
from django.contrib import admin

# Models
from posts.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('pk', 'user', 'profile', 'title', 'photo')
    list_display_links = ('pk', 'user')
    list_editable = ('title', 'photo')

    search_fields = ('title',)

    list_filter = ('created', 'modified')

    fieldsets = (
        ('Post', {
            'fields': (('pk', 'title'),),
        }),
        ('Extra info', {
            'fields': (('user', 'profile'),),
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        }),
    )
