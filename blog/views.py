from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': "Maha Amin",
        'title': "Blog Post 1",
        'content': 'First post content.',
        'date_posted': 'March 20 2020'
    },
    {
        'author': "Nayera Mohamed",
        'title': "Blog Post 2",
        'content': 'Second post content.',
        'date_posted': 'March 22 2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "About!"})
