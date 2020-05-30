from django.shortcuts import render, reverse, HttpResponseRedirect
from twitterclone.twitteruser.forms import SignupForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.models import Tweet
from twitterclone.notification.models import Notification



def signup_view(request):
    """Allows a user to sign up"""
    html = "generic.html"
    header = "Signup"
    form = None
    button_value = "Signup"
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data["username"], password=data["password"])
            login(request, user)
            TwitterUser.objects.create(
                username=data["username"],
                display_name=data["display_name"],
                user=user
            )
            return HttpResponseRedirect(reverse("home"))
    else:
        form = SignupForm()
    return render(request, html, {"header": header, "form": form,
                                  "button_value": button_value})


def profile_view(request, username):
    """See a user's profile"""
    html = "twitteruser.html"
    targeteduser = TwitterUser.objects.filter(username=username).first()
    targeteduser_tweets = Tweet.objects.filter(
        user=targeteduser).order_by("-date")
    num_tweets = len(targeteduser_tweets)
    num_followers = targeteduser.following.count()
    follow_status_button = None
    data = {}
    if request.user.is_authenticated:
        currentuser = TwitterUser.objects.filter(
            username=request.user.twitteruser).first()
        notifications = Notification.objects.filter(username=currentuser).count()
        if targeteduser not in currentuser.following.get_queryset():
            follow_status_button = "Follow"
        else:
            follow_status_button = "Unfollow"
        data = {"targeteduser": targeteduser, "tweets": targeteduser_tweets,
                "num_tweets": num_tweets,
                "follow_status_button": follow_status_button,
                "num_followers": num_followers,
                "notifications": notifications}
    else:
        data = {"targeteduser": targeteduser, "tweets": targeteduser_tweets,
                "num_tweets": num_tweets, "num_followers": num_followers}
    return render(request, html, data)


def follow_view(request, username):
    """Follower's info"""
    html = "follow.html"
    header = "Following"
    is_following = False
    targeteduser = TwitterUser.objects.filter(username=username).first()
    currentuser = TwitterUser.objects.filter(
        username=request.user.twitteruser).first()
    if targeteduser not in currentuser.following.get_queryset():
        currentuser.following.add(targeteduser)
        is_following = True
    else:
        currentuser.following.remove(targeteduser)
        is_following = False
    currentuser.save()
    return render(request, html, {"header": header,
                     "is_following": is_following})