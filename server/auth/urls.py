from django.contrib import admin
from django.urls import path, include
from auth.views import AuthView

urlpatterns = [
    path('token/', AuthView.as_view(), name="create_token")
]
