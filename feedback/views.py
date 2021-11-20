from .forms import CommentForm
from django.shortcuts import render, redirect, get_object_or_404


def feedback(request):
    """ A view that renders the feedback contents page """

    form = CommentForm()

    return render(request, 'feedback/feedback.html')


def post_detail(request, slug):
    template_name = 'post_detail.html'
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return redirect(template_name, slug=post.slug)
                                           
