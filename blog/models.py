from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Defines the Post Model
    """
    title = models.CharField(max_length=200, unique=True,
                             default="Some String")
    slug = models.SlugField(max_length=200, unique=True,
                            null=True, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """
        Innerclass of Post model, affects the behaviour of the fields.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string representation
        """
        return self.title

    def number_of_likes(self):
        """
        Returns the number of likes
        using built in python function count()
        """
        return self.likes.count()

    def get_absolute_url(self):
        """
        Returns the full URL to the home route as a string
        """
        return reverse('home')

    def number_of_comments(self):
        """
        Returns the number of comments
        using built in python function count()
        """
        return self.comments.count()


class Comment(models.Model):
    """
    Defines the Comment Model
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Innerclass of Post model, affects the behaviour of the fields.
        """
        ordering = ['created_on']

    def __str__(self):
        """
        Returns a string representation of the Comment Model
        """
        return f"Comment {self.body} by {self.name}"


class ContactEnquiry(models.Model):
    """
    Defines the Comment Model
    """
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=80, blank=True)
    message = models.TextField(blank=True)
    subject = models.CharField(max_length=60, blank=True)
    completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        """
        Returns a string representation of the name object
        """
        return self.name
