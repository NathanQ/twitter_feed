import os
import datetime


PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

INSTALLED_APPS = (
    # list this with your apps
    'twiiter_feed',
)

TWITTER_KEYS = {
    "consumer_key":"#your consumer key", 
    "consumer_secret":"#your consumer secret from twitter",
    "access_token":"#your access token from twitter",
    "access_token_secret":"#your access token secret from twitter",
    }
    
TWITTER_NAME = "NateVictor"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}