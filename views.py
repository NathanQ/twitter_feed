import json
import tweepy
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings
from django.core.cache import cache

from .stream import get_twitter_api


def status_stream_json(request):
    twitter = get_twitter_api()    
    key = "twitter_stream"           
    payload = cache.get(key)
    if not payload:
        status_stream = twitter.user_timeline(screen_name=settings.TWITTER_NAME,count=5)
        payload = json.dumps(status_stream._payload)
        cache.set(key, payload, 60*5)

    return HttpResponse(payload, content_type='application/json')