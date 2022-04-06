from django.conf import settings
from django.utils.module_loading import import_string

UserSerializer = import_string(settings.AUTH_USER_SERIALIZER)


def get_serializer_user_in_profile_type(user, request):

    profiles = {
        "seller": import_string(settings.AUTH_SELLER_SERIALIZER),
        "customer": import_string(settings.AUTH_CUSTOMER_SERIALIZER)
    }

    for profile in profiles:
        if user.profile == profile:
            if user.profile == "seller":
                user = user.seller
            else:
                user = user.customer

            return profile, profiles[profile](instance=user, context={"request": request}).data

    return "admin", UserSerializer(instance=user)



