from django.contrib import admin
from .models import Category, Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_time', 'modified_time']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)