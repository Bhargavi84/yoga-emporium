from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Feedback
from .forms import CommentForm


def feedbacks(request):
    feedbacks = Feedback.objects.filter(status=1).order_by('-created_on')

    template = 'feedbacks/feedbacks.html'
    return render(request, template, {'feedbacks':feedbacks})


def comments_details(request, slug):
    template_name = 'feedbacks/comments_details.html'
    feedback = get_object_or_404(Feedback, slug=slug)
    comments = feedback.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.feedback = feedback
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'feedback': feedback,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})