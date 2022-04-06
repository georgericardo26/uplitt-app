from oauth2_provider.models import Application
from django.urls import reverse
from django.test import Client


class GetTokenTest:

    def __init__(self):
        app = Application(name='app_test', client_type='confidential',
                          authorization_grant_type='password')
        app.save()

        self.data = {
            "client_id": app.client_id,
            "client_secret": app.client_secret,
            "grant_type": "password"
        }

    def get_token(self, username, password):
        client = Client()
        data = {
            **self.data,
            "username": username,
            "password": password
        }
        return client.post(
            reverse('oauth2_provider:token'),
            data=data,
            content_type='application/json')
