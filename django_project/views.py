from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from django.conf import settings


class CustomGoogleOAuth2Adapter(GoogleOAuth2Adapter):
    basic_auth = False


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = CustomGoogleOAuth2Adapter
    callback_url = settings.GOOGLE_CALLBACK_URL #"http://localhost:8000/accounts/google/login/callback/"
    client_class = OAuth2Client
