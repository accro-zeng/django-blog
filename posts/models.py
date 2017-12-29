from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def abs_url(self):
        return reverse(
            'posts:detail', kwargs={
                'id': self.id
            })  # 依据数据库的id和网页结构给每篇文章生成网址

