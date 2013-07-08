import tweepy
import simplejson as json
from django.conf import settings


class MyModelParser(tweepy.parsers.ModelParser):
    """
    https://gist.github.com/inactivist/5263501
    api = tweepy.API(auth, parser=MyModelParser())
    results = api.user_timeline(screen_name='twitter')
 
    for s in results._payload:
        print  json.dumps(s)
    """
    
    def parse(self, method, payload):
        result = super(MyModelParser, self).parse(method, payload)
        result._payload = json.loads(payload)
        return result


def get_twitter_api():
    auth = tweepy.OAuthHandler(settings.TWITTER_KEYS['consumer_key'], settings.TWITTER_KEYS['consumer_secret'])
    auth.set_access_token(settings.TWITTER_KEYS['access_token'], settings.TWITTER_KEYS['access_token_secret'])
    return tweepy.API(auth, parser=MyModelParser())

