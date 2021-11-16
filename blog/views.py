from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm

# Create your views here.

def view_blog(request):
    """ A view that renders the bag contents page """

    return render(request, 'blog/blog.html')