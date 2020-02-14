from django.shortcuts import render
from posts.models import Post


def home(request):

    home_posts = Post.objects.all()[:3]
    context = {"title": "title", 'post_list' : home_posts}
    return render(request, 'landing/home.html', context)

def contact(request):
    return render(request, 'landing/contact.html')

def about(request):
    return render(request, 'landing/about.html')
