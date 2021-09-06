from django.urls import path
from rest_framework import routers

from portal.views import PollOptions, Polls, PollVotes, RetrievePollVotes


router = routers.DefaultRouter()
router.register(r"polls", Polls)
router.register(r"options", PollOptions)
router.register(r"votes", PollVotes)

additional_urls = [path("poll-history/", RetrievePollVotes.as_view(), name="poll-history")]
urlpatterns = router.urls + additional_urls
