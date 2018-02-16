# Create your views here.
import tweepy
from django.http import *
from django.urls import reverse
from django.contrib.auth import logout
from django.shortcuts import render_to_response

from .utils import get_api, get_oauth


def index(request):
    """
    index view of app, either login page or info page
    """
    # if we haven't authorised yet, direct to login page
    if check_key(request):
        return HttpResponseRedirect(reverse('info'))
    else:
        return render_to_response('unfollow/login.html')


def unauth(request):
    """
    logout and remove all session data
    """
    if check_key(request):
        api = get_api(request)
        request.session.clear()
        logout(request)
    return HttpResponseRedirect(reverse('index'))


def info(request):
    """
    display some user info to show we have authenticated successfully
    """
    print(check_key)
    if check_key(request):
        api = get_api(request)
        user = api.me()
        return render_to_response('unfollow/info.html', {'user' : user})
    else:
        return HttpResponseRedirect(reverse('index'))


def auth(request):
    # start the OAuth process, set up a handler with our details
    oauth = get_oauth()
    # direct the user to the authentication url
    # if user is logged-in and authorized then transparently goto the callback URL
    auth_url = oauth.get_authorization_url(True)
    response = HttpResponseRedirect(auth_url)
    # store the request token
    request.session['request_token'] = oauth.request_token
    return response


def callback(request):
    verifier = request.GET.get('oauth_verifier')
    oauth = get_oauth()
    token = request.session.get('request_token')
    # remove the request token now we don't need it
    request.session.delete('request_token')
    oauth.request_token = token
    # get the access token and store
    try:
        oauth.get_access_token(verifier)
    except tweepy.TweepError:
        print('Error, failed to get access token')

    request.session['access_key_tw'] = oauth.access_token
    request.session['access_secret_tw'] = oauth.access_token_secret
    print(request.session['access_key_tw'])
    print(request.session['access_secret_tw'])
    response = HttpResponseRedirect(reverse('info'))
    return response


def check_key(request):
    """
    Check to see if we already have an access_key stored, if we do then we have already gone through
    OAuth. If not then we haven't and we probably need to.
    """
    try:
        access_key = request.session.get('access_key_tw', None)
        if not access_key:
            return False
    except KeyError:
        return False
    return True
