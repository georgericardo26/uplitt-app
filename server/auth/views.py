import json

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.utils.module_loading import import_string
from django.views.decorators.debug import sensitive_post_parameters
from oauth2_provider.views import TokenView

from auth.helpers import get_serializer_user_in_profile_type

User = get_user_model()
UserSerializer = import_string(settings.AUTH_USER_SERIALIZER)


class AuthView(TokenView):

    @method_decorator(sensitive_post_parameters("password"))
    def post(self, request, *args, **kwargs):
        url, headers, body, status = self.create_token_response(request)

        if status == 200:
            user_request = json.loads(request.body.decode("utf-8"))
            username = user_request.get("username")
            user = User.objects.get(username=username)

            profile, serializer = get_serializer_user_in_profile_type(user, request)

            body = json.loads(body)
            body[profile] = serializer
            body = json.dumps(body)

        return HttpResponse(content=body, status=status)
