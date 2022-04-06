from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import serializers

from core.api.v1.business import create_or_get_ingredients
from core.api.v1.serializers.serializers_food_item_category import (
    FoodItemCategorySerializer,
    FoodItemCategoryHyperlinkedIdentitySerializer
)
from core.api.v1.serializers.serializers_igredient_item import IngredientItemToFoodItemCreateSerializer, \
    IngredientItemSerializer
from core.api.v1.serializers.serializers_image import ImageSerializer
from core.api.v1.serializers.serializers_tag_food_item import TagFoodItemSerializer
from core.api.v1.validators import duplicated_name_to_ingredient_item_validator
from core.models import FoodItemCategory, FoodItem, Image, IngredientItem
from core.models.models_store import IngredientChosenToFoodItem


class FoodItemBaseSerializer(serializers.ModelSerializer):
    image = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=Image.objects.all(),
        write_only=True,
        required=False
    )
    food_item_image = serializers.SerializerMethodField()

    class Meta:
        model = FoodItem
        fields = ["id", "title", "description", "price", "image", "food_item_image"]

    def get_food_item_image(self, obj):
        serializer = ImageSerializer(instance=obj.image, context=self.context)
        return serializer.data


class FoodItemSerializer(FoodItemBaseSerializer):
    foodItemCategory = serializers.PrimaryKeyRelatedField(
        many=False,
        queryset=FoodItemCategory.objects.all(),
        required=False)

    ingredients = IngredientItemToFoodItemCreateSerializer(many=True, required=False)

    class Meta(FoodItemBaseSerializer.Meta):
        fields = [
            "id",
            "title",
            "description",
            "ingredients",
            "price",
            "tags",
            "food_item_image",
            "image",
            "foodItemCategory",
            "updateAt",
            "createAt"
        ]
        validators = [duplicated_name_to_ingredient_item_validator]

    def create(self, validated_data):
        ingredients = validated_data.pop("ingredients")

        fooditem_instance = super(FoodItemSerializer, self).create(validated_data)
        virtualshop = fooditem_instance.foodItemCategory.virtualshop
        new_ingredients = []

        try:

            for item in ingredients:

                if not IngredientItem.objects.filter(
                        name=item["name"],
                        virtualshop__pk=virtualshop.pk).exists():

                    ingredient = IngredientItem(
                        name=item["name"],
                        details=item.get("detail"),
                        virtualshop=virtualshop
                    )

                    ingredient.full_clean()
                    ingredient.save()
                    new_ingredients.append(ingredient)
                else:
                    ingredient = IngredientItem.objects.get(
                        name=item["name"],
                        virtualshop__pk=virtualshop.pk)
                    new_ingredients.append(ingredient)

        except ValidationError:
            return serializers.ValidationError("Error to save Ingredients")

        try:
            fooditem_instance.ingredients.set(new_ingredients)
            fooditem_instance.save()

        except Exception:
            return serializers.ValidationError("Error to insert ingredients to food item")

        return fooditem_instance

    def update(self, instance, validated_data):
        ingredients = validated_data.pop("ingredients")
        instance = super(FoodItemSerializer, self).update(instance, validated_data)

        virtualshop = instance.foodItemCategory.virtualshop

        try:
            # Create ingredients
            ingredients_returned = create_or_get_ingredients(instance,
                                                             IngredientItem,
                                                             IngredientChosenToFoodItem,
                                                             ingredients,
                                                             virtualshop)
        except ValidationError:
            return serializers.ValidationError("Error to save Ingredients")

        try:
            instance.ingredients.set(ingredients_returned)
            instance.save()
        except Exception:
            return serializers.ValidationError("Error to insert ingredients to food item")

        return instance


class FoodItemOutputSerializer(FoodItemSerializer):

    foodItemCategory = FoodItemCategoryHyperlinkedIdentitySerializer(read_only=True, required=False)
    virtualshop = serializers.SerializerMethodField()
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )
    ingredients = IngredientItemSerializer(many=True, read_only=True)

    class Meta(FoodItemBaseSerializer.Meta):
        fields = [
            "id",
            "title",
            "description",
            "ingredients",
            "price",
            "tags",
            "food_item_image",
            "image",
            "foodItemCategory",
            "virtualshop",
            "updateAt",
            "createAt"
        ]

    def get_virtualshop(self, obj):
        return {
            "id": obj.foodItemCategory.virtualshop.pk,
            "name": obj.foodItemCategory.virtualshop.name
        }


class FoodItemIngredientListSerializer(serializers.ModelSerializer):

    foodItemCategory = FoodItemCategorySerializer(read_only=True)

    class Meta:
        model = FoodItem
        fields = [
            "id",
            "title",
            "description",
            "price",
            "image",
            "foodItemCategory"
        ]


class FoodItemUpdateSerializer(serializers.ModelSerializer):

    foodItemCategory = FoodItemCategorySerializer(read_only=True)

    class Meta:
        model = FoodItem
        fields = "__all__"
