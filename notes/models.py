from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Note(models.Model):
    week_days = [
        ('Monday', 'Moday')
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    note_text = models.TextField()
    date_created = models.DateField(auto_now=True)
    day_planned = models.CharField(max_length=9, choices=week_days)

    def get_absolute_url(self):
        return reverse('notes:note_list')

    def __str__(self):
        return self.user.username
