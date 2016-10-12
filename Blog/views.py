from django.shortcuts import render
from Blog.models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Blog/post_list.html', {'posts': posts})
