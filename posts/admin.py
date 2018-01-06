from django.contrib import admin
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_time', 'modified_time']

    def get_ordering(self, request):
        return ['-created_time']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)