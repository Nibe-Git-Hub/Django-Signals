from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tweet
from History.models import History

@receiver(post_save, sender=Tweet)
def create_history_on_tweet_save(sender, instance, created, **kwargs):
    if created:
        # Only runs this logic if a new Tweet object was created.
        summary = f"User {instance.user.username} Created tweet with a content of '{instance.content}' at {instance.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
        History.objects.create(
            user=instance.user,
            method='POST',
            tweet=instance,
            date=instance.created_at,
            summary=summary
        )