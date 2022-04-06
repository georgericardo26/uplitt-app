from django.urls import path
from core.api.v1.views.account_views import (
    SellerCreateView,
    SellerRetrieveUpdateDestroyView,
    CustomerCreateView,
    CustomerRetrieveUpdateDestroyView,
)

app_name = "account"

urlpatterns = [
    path("sellers/", SellerCreateView.as_view(), name="create_seller"),
    path(
        "sellers/<int:pk>/",
        SellerRetrieveUpdateDestroyView.as_view(),
        name="retrieve_update_destroy_seller",
    ),
    path("customers/", CustomerCreateView.as_view(), name="create_customer"),
    path("customers/<int:pk>/", CustomerRetrieveUpdateDestroyView.as_view(), name="retrieve_update_destroy_customer"),
]
