from django.db import models
from tweet.models import Tweet
from twitteruser.models import TwitterUser


class Notification(models.Model):
    mentioned = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    mention_tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    mark_as_read = models.BooleanField(default=False)