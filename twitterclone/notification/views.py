from django.shortcuts import render, reverse, HttpResponseRedirect
from twitterclone.notification.forms import NotificationForm
from django.contrib.auth.models import User
from twitterclone.notification.models import Notification
from django.contrib.auth.decorators import login_required
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.models import Tweet



@login_required()
def notification_view(request):
    html = "notifications.html"
    currentuser = TwitterUser.objects.filter(
        user=request.user).first()
    notifications = Notification.objects.filter(username=currentuser)
    for notice in notifications:
        notice.delete()
    return render(request, html, {"notifications": notifications})