from django.urls import path
from twitterclone.twitteruser.views import (signup_view, profile_view, follow_view)

urlpatterns = [
    path("signup/", signup_view),
    path("<str:username>/", profile_view),
    path("follow/<str:username>/", follow_view),
]
