from django.shortcuts import render, HttpResponseRedirect, reverse
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from .models import Notification
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def notification_view(request):
    tweets = Notification.objects.filter(mentioned=request.user)
    notification_count = 0
    notif_list = []
    for tweet in tweets:
        if tweet.mark_as_read == False:
            notification_count += 1
            notif_list.append(tweet.mention_tweet)
            tweet.mark_as_read = True
            tweet.save()
    return render(request, 'notifications.html', {'mentions': notif_list, 'count': notification_count})


def notification_count_view(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(mentioned=request.user)
        notification_count = 0
        for notification in notifications:
            if notification.mark_as_read == False:
                notification_count += 1
    else:
        notification_count = 0
    return notification_count