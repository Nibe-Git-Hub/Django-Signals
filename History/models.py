from django.db import models
from django.contrib.auth.models import User
from Tweet.models import Tweet

# Create your models here.

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    method = models.CharField(max_length=10) # e.g., 'POST'
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()

    def __str__(self):
        return self.summary