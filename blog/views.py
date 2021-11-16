from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404

def view_blog(request):
    """ A view to return to index page """

    return render(request, 'blog/blog.html')

