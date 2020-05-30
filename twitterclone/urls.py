from django.contrib import admin
from django.urls import path
from twitterclone.authentication.urls import urlpatterns as authentication_urls
from twitterclone.notification.urls import urlpatterns as notification_urls
from twitterclone.tweet.urls import urlpatterns as tweet_urls
from twitterclone.twitteruser.urls import urlpatterns as twitteruser_urls
from twitterclone.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view, name="home")
]

urlpatterns += authentication_urls
urlpatterns += notification_urls
urlpatterns += tweet_urls
urlpatterns += twitteruser_urls

