import tweepy
from django.conf import settings


def get_oauth():
    return tweepy.OAuthHandler(settings.TWITTER['API_KEY'],
                               settings.TWITTER['API_SECRET'])


def get_api(request):
    # set up and return a twitter api object
    oauth = get_oauth()
    access_key = request.session['access_key_tw']
    access_secret = request.session['access_secret_tw']
    oauth.set_access_token(access_key, access_secret)
    api = tweepy.API(oauth)
    return api
