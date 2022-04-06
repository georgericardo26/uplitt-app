import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from core.api.v1.filters import VirtualShopListFilter

from core.api.v1.serializers.serializers_food_item import FoodItemOutputSerializer
from core.api.v1.serializers.serializers_igredient_item import IngredientItemSerializer

from core.api.v1.serializers.serializers_regions import (
    AddressSerializer,
    AddressVirtualShopUpdateSerializer
)
from core.api.v1.serializers.serializers_tag_food_item import TagFoodItemSerializer

from core.api.v1.serializers.serializers_virtualshop import (
    VirtualShopSerializer,
    VirtualShopUpdateSerializer,
    VirtualShopListFoodItemCategorySerializer, 
    VirtualShopListIngredientItemSerializer,
    VirtualShopSearchListSerializer
)

from core.api.v1.serializers.serializers_virtual_shop_category import (
    VirtualShopCategorySerializer,
    VirtualShopCategoryUpdateSerializer,
)


from core.api.v1.serializers.serializers_food_item_category import (
    FoodItemCategorySerializer,
    FoodItemCategoryUpdateSerializer,
)

from core.api.v1.serializers.serializers_food_item import (
    FoodItemSerializer,
    FoodItemUpdateSerializer,
)

from core.api.v1.serializers.serializers_image import ImageSerializer

from core.api.v1.serializers.serializers_food_item_option import (
    FoodItemOptionListCreateSerializer,
    FoodItemOptionRetrieveUpdateDestroySerializer,
)

from core.api.v1.serializers.serializers_opening_hour import OpeningHourSerializer

from core.api.v1.serializers.serializers_weekdays import WeekdaysSerializer, WeekdaysListOpeningHourSerializer

from core.models import (
    Seller,
    VirtualShop,
    FoodItemCategory,
    FoodItem,
    Address,
    Image,
    VirtualShopCategory,
    FoodItemOption,
    OpeningHour,
    Weekdays, TagFoodItem, IngredientItem, IngredientChosenToFoodItem,
)

logger = logging.getLogger(__name__)


class VirtualShopCreateView(generics.ListCreateAPIView):
    queryset = VirtualShop.objects.all()
    serializer_class = VirtualShopSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination
    # filter_class = VirtualShopListFilter

    def create(self, request, *args, **kwargs):

        # Get the seller id from request.user
        seller = get_object_or_404(Seller, user__pk=request.user.pk)
        request.data["seller"] = seller.pk

        return super(VirtualShopCreateView, self).create(request, *args, **kwargs)

class VirtualShopSearchListView(generics.ListAPIView):
    queryset = VirtualShop.objects.all()
    serializer_class = VirtualShopSearchListSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination
    filter_class = VirtualShopListFilter


class VirtualShopRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = VirtualShop.objects.all()
    serializer_class = VirtualShopSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def update(self, request, *args, **kwargs):

        # Get the seller id from request.user
        seller = get_object_or_404(Seller, user__pk=request.user.pk)
        request.data["seller"] = seller.pk

        return super(VirtualShopRetrieveUpdateView, self).update(
            request, *args, **kwargs
        )


class VirtualShopRetrieveUpdateAddressView(generics.RetrieveUpdateAPIView):

    queryset = VirtualShop.objects.all()
    serializer_class = AddressVirtualShopUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
    lookup_field = "pk"

    def get_object(self):
        obj = super(VirtualShopRetrieveUpdateAddressView, self).get_object()
        return obj.address

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        if not partial:
            return Response(data={"detail": "Method not allowed for this resource, try PATCH instead."}, status=405)

        return super(VirtualShopRetrieveUpdateAddressView, self).update(request, *args, **kwargs)


class VirtualShopListFoodItemCategoryView(generics.ListAPIView):
    queryset = FoodItemCategory.objects.all()
    serializer_class = VirtualShopListFoodItemCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination
    lookup_field = "pk"

    def list(self, request, *args, **kwargs):
        # Get the seller id from request.user
        seller = get_object_or_404(Seller, user__pk=request.user.pk)

        self.queryset = FoodItemCategory.objects.filter(
            virtualshop__pk=seller.virtualshop.pk
        )

        return super(VirtualShopListFoodItemCategoryView, self).list(
            request, *args, **kwargs
        )


class VirtualShopListIngredientItemView(generics.RetrieveUpdateAPIView):
    queryset = IngredientItem.objects.all()
    serializer_class = VirtualShopListIngredientItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination
    lookup_field = "pk"

    def retrieve(self, request, *args, **kwargs):
        virtualshop = get_object_or_404(VirtualShop, pk=kwargs.get("pk"))
        ingredients = IngredientItem.objects.filter(virtualshop=virtualshop.pk)

        serializer = self.serializer_class(many=True, data=ingredients, context={"request", request})
        serializer.is_valid()

        return Response(data=serializer.data, status=200)


class VirtualShopCategoryCreateView(generics.ListCreateAPIView):
    queryset = VirtualShopCategory.objects.all()
    serializer_class = VirtualShopCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class VirtualShopCategoryRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = VirtualShopCategory.objects.all()
    serializer_class = VirtualShopCategoryUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class FoodItemCategoryCreateListView(generics.ListCreateAPIView):
    queryset = FoodItemCategory.objects.all()
    serializer_class = FoodItemCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','virtualshop__name']

    def list(self, request, *args, **kwargs):
        # Get the seller id from request.user
        seller = get_object_or_404(Seller, user__pk=request.user.pk)

        self.queryset = FoodItemCategory.objects.filter(virtualshop__pk=seller.virtualshop.pk)

        return super(FoodItemCategoryCreateListView, self).list(
            request, *args, **kwargs
        )


class FoodItemCategoryRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodItemCategory.objects.all()
    serializer_class = FoodItemCategoryUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class TagFoodItemListCreateView(generics.ListCreateAPIView):
    queryset = TagFoodItem.objects.all()
    serializer_class = TagFoodItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination


class IngredientItemListCreateView(generics.ListCreateAPIView):
    queryset = IngredientItem.objects.all()
    serializer_class = IngredientItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

class IngredientItemRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = IngredientItem.objects.all()
    serializer_class = IngredientItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination


class FoodItemListCreateView(generics.ListCreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class FoodItemRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemOutputSerializer
    serializer_class_input = FoodItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def update(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        instance = FoodItem.objects.get(pk=pk)
        serializer_input = self.serializer_class_input(data=request.data,
                                                       instance=instance,
                                                       context={"request": request},
                                                       partial=True)
        serializer_input.is_valid(raise_exception=True)
        serializer_input.save()

        serializer_output = self.serializer_class(instance=serializer_input.instance,
                                                  context={"request": request})

        return Response(data=serializer_output.data, status=200)


class FoodItemDeleteIngredientView(generics.DestroyAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemOutputSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def destroy(self, request, *args, **kwargs):
        foodItem = get_object_or_404(FoodItem, pk=kwargs.get("pk"), ingredients__pk=request.data.get("id"))
        ingredient_item = get_object_or_404(IngredientItem, pk=request.data.get("id"))

        foodItem.ingredients.remove(ingredient_item)

        return Response(status=204)


class FoodItemOptionListCreateView(generics.ListCreateAPIView):
    queryset = FoodItemOption.objects.all()
    serializer_class = FoodItemOptionListCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class FoodItemOptionRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodItemOption.objects.all()
    serializer_class = FoodItemOptionRetrieveUpdateDestroySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class ImageListCreateView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination


class ImageRetrieveView(generics.RetrieveDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class OpeningHourCreateView(generics.CreateAPIView):
    queryset = OpeningHour.objects.all()
    serializer_class = OpeningHourSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


class WeekdaysListView(generics.ListAPIView):
    queryset = Weekdays.objects.all()
    serializer_class = WeekdaysSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

class WeekdaysListOpeningHourView(generics.RetrieveAPIView):
    serializer_class = WeekdaysListOpeningHourSerializer
    pagination_class = None

    def retrieve(self, request, *args, **kwargs):
        company_id = kwargs.get("company_pk")
        weekdays = Weekdays.objects.filter(opening_hours__virtualShop__pk=company_id).distinct()

        serializer = self.serializer_class(data=weekdays, many=True, context={'request': request})
        serializer.is_valid()

        return Response(data=serializer.data, status=200)
