from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.views.generic import CreateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, BlogPost
from django.forms import ModelForm
from django.utils.text import slugify


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


def post_detail(request, slug, *arghs, **kwargs):

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by('created_on')
    comment_count = post.comments.filter(approved=True).count()
    liked = False
    commeted = False

    if post.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment awaiting moderation')  # noqa
        else:
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(
        request,
        "post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "commented": False,
            "liked": liked,
            "comment_form": comment_form
        }
    )


def post_like(request, slug, *arghs, **kwargs):

    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST" and request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id, *args, **kwargs):

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = post.comments.filter(id=comment_id).first()

    if comment.name == request.user.username:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment Successfully Deleted.')  # noqa
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments.')  # noqa

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_edit(request, slug, comment_id, *args, **kwargs):
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
            messages.add_message(request, messages.SUCCESS, 'Your Comment has been Updated!')  # noqa
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')  # noqa

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def search_recipes(request):

    if request.method == "POST":
        search = request.POST["search"]
        recipes = Post.objects.filter(title__contains=search)

        return render(
            request, "search_recipes.html", {"search": search, "recipes": recipes}  # noqa
        )
    else:
        return render(request, "search_recipes.html", {})


class AddPostView(CreateView):
    model = Post
    template_name = 'user_post.html'
    fields = ("title", "content", "featured_image", "excerpt", "status")  # noqa

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def save(self, *args, **kwargs):
        self.slug = unique_slugify(self.title)
        super(Post, self).save(*args, **kwargs)
