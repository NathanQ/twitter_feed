from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('twitter_feed.views',
    url(r'^json/$', 'status_stream_json', name='status_stream_json'),
)