from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.views.generic import CreateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, ContactEnquiry
from .forms import CommentForm, BlogPost, ContactForm
from django.forms import ModelForm
from django.utils.text import slugify

"""
Constants for messages to prevent PEP8 errors
"""
MODERATION = 'Comment awaiting moderation'
SUCCESSFULLY_DELETED = 'Comment Successfully Deleted.'
DELETE_FAILED = 'You can only delete your own comments.'
COMMENT_UPDATED = 'Your Comment has been Updated!'
UPDATE_FAILED = 'Error updating comment!'
CONTACT_SUCCESS = 'Luca has received your message and will respond ASAP.'
CONTACT_FAILED = 'Error sending message!'


class PostList(generic.ListView):
    """
    Handles the blogposts displayed on homepage.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


def post_detail(request, slug, *arghs, **kwargs):
    """
    Defines the logic for blog post page.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by('created_on')
    comment_count = post.comments.filter(approved=True).count()
    liked = False
    commented = False

    if post.likes.filter(id=request.user.id).exists():
        liked = True

    comment_form = CommentForm()  # Initialize unbound form first

    if request.method == "POST" and request.user.is_authenticated:
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, MODERATION)

    return render(
        request,
        "post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "liked": liked,
            "comment_form": comment_form
        }
    )


def post_like(request, slug, *arghs, **kwargs):
    """
    Defines the logic for liking a blog post.
    """

    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST" and request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id, *args, **kwargs):
    """
    Handles the logic to allow a user to delete a comment
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = post.comments.filter(id=comment_id).first()

    if comment.name == request.user.username:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, SUCCESSFULLY_DELETED)
    else:
        messages.add_message(request, messages.ERROR, DELETE_FAILED)

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_edit(request, slug, comment_id, *args, **kwargs):
    """
    Handles the logic to allow a user to edit their own comment
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = post.comments.filter(id=comment_id).first()

        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.name == request.user.username:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, COMMENT_UPDATED)
        else:
            messages.add_message(request, messages.ERROR, UPDATE_FAILED)

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def search_recipes(request):
    """
    Handles the logic to allow a user to search for blog recipes
    """

    if request.method == "POST":
        search = request.POST["search"]
        recipes = Post.objects.filter(title__icontains=search)

        return render(
            request, "search_recipes.html", {"search": search,
                                             "recipes": recipes}
        )
    else:
        return render(request, "search_recipes.html", {})


def contact_form(request):
    "Handles the logic for the contact form"
    form_class = ContactForm

    form = form_class(request.POST)
    if request.method == "POST":
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            msg = request.POST.get('message')
            contact.completed = False
            form.save()
            messages.add_message(request, messages.SUCCESS, CONTACT_SUCCESS)
            return HttpResponseRedirect('/contact_luca')
        else:
            messages.add_message(request, messages.ERROR, CONTACT_FAILED)

    return render(request, 'contact.html', {'form': form})
