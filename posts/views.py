from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    allpost = Post.objects.all().order_by('-created_time')
    for post in allpost:
        post.content = markdown.markdown(
            post.content,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ])
    paginator = Paginator(allpost, 2)
    page = request.GET.get('page')
    try:
        post_list = paginator.get_page(page)
    except PageNotAnInteger:
        post_list = paginator.get_page(1)
    except EmptyPage:
        post_list = paginator.get_page(paginator.num_pages)
    return render(request, 'index.html', context={'post_list': post_list})


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    post.content = markdown.markdown(
        post.content,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
    return render(request, 'detail.html', context={'post': post})
