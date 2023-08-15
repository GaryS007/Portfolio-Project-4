from .models import Comment, Post, ContactEnquiry
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
        model = ContactEnquiry
        fields = ('name', 'email', 'subject', 'message',)
        labels = {
            'name': (''),
            'email': (''),
            'subject': (''),
            'message': (''),

        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter Your Name',
                'class': 'form-control',
                'style': 'max-width: 300px',
                }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Enter your Email',
                'class': 'form-control',
                'style': 'max-width: 300px',
                }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Subject Line',
                'class': 'form-control',
                'style': 'max-width: 300px',
                }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Enter your Message',
                'class': 'form-control',
                'style': 'max-width: 300px',
                }),
        }
