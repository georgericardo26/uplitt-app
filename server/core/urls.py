from django.urls import include, path, re_path

app_name = "api"

urlpatterns = [
    path('v1/', include('core.api.urls.v1_urls', namespace='v1')),
]
