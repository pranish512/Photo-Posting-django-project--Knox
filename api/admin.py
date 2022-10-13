from django.contrib import admin
from .models import PostModel

# Register your models here.

# class PostPanel(admin.ModelAdmin):
#     list_display: ['post_id', 'post_name', 'date']
#     ordering: ['post_id']

admin.site.register(PostModel)

