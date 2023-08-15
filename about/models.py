from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Defines the Comment Model
    """
    title = models.CharField(max_length=200, unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()

    def __str__(self):
        """
        Returns a string representation of the title object
        """
        return self.title
