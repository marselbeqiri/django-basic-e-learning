from django.db import models
from django.utils import timezone

from poll.models import Question, Choice # BEjme import modelin e app poll

from main.models import Tutorial #  BEjme import modelin e app main

# Modeli i Koment  per Poll app

class Comment_Poll(models.Model):
    post = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


# Modeli i Koment  per main app
class Comment_main(models.Model):
    post = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text        