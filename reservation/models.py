from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

TIME_CHOICES = (
    ("12 PM", "12 PM"),
    ("1 PM", "1 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
)


class Appointment(models.Model):
    day = models.DateField(default=datetime.now)
    time = models.Charfield(max_length=10, choices=TIME_CHOICES, default="3 PM")  # noqa
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"
