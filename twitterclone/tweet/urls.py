from django.urls import path
from twitterclone.tweet.views import (tweet_creation_view, tweet_view)


urlpatterns = [
    path("tweet/", tweet_creation_view, name="tweet"),
    path("tweets/", tweet_view),
    path("tweet/<int:id>/", tweet_view, name="tweet")

]