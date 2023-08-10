from .models import Comment, Post, Contact
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class BlogPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'author',
            'featured_image',
            'excerpt',
            'content',
            'status',
            'likes',
            )

        def __init__(self, *args, **kwargs):
            super(AddPostView, self).__init__(*args, **kwargs)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'message',
        )
