from django.db import models
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

from core.helpers import directory_path
from core.models import Address, Seller


class Image(models.Model):
    upload = models.ImageField(null=True, blank=True, upload_to=directory_path)
    name = models.CharField(max_length=50, blank=True, null=True)
    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)

    def filename(self):
        return self.upload.name

    def __repr__(self):
        return f"<Image: {self.name}>"

    def __str__(self):
        return self.name or "Unknown"


class VirtualShopCategory(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)

    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)

    def __repr__(self):
        return f"<Title: {self.title}>"

    def __str__(self):
        return self.title


class VirtualShop(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    phoneNumber = models.CharField(max_length=20, blank=True, null=True)

    seller = models.OneToOneField(
        Seller, blank=False, null=False, on_delete=models.CASCADE
    )

    address = models.ForeignKey(
        Address, blank=True, null=True, on_delete=models.SET_NULL
    )

    virtualShopCategory = models.ManyToManyField(
        VirtualShopCategory,
        null=True,
        blank=True,
    )

    image = models.OneToOneField(
        Image, blank=True,
        null=True,
        on_delete=models.SET_NULL
    )

    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)

    def __repr__(self):
        return f"<VirtualShop: {self.name}>"

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ["seller"]


class FoodItemCategory(models.Model):
    """
    This Model will contain each category food that belong to virtualshop
    """
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=250, blank=False, null=False)

    virtualshop = models.ForeignKey(
        VirtualShop,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="foodItemCategories"
    )

    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)

    def __repr__(self):
        return f"<FoodItemCategory: {self.title}>"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Food Item Category"
        verbose_name_plural = "Food Item Categories"


class TagFoodItem(models.Model):
    """
    This Model is responsable to create tags to identify the type of FOOD
    The cardinality to FoodItem model is One-To-Many
    """
    COLORS = [
        ("#ff0000", "Red"),
        ("#007fff", "Blue"),
        ("#9edeff", "Light Blue"),
        ("#3ff8ff", "Purple"),
        ("#3fffaf", "Light Green"),
        ("#00e070", "Gree"),
        ("#fff200", "Yellow"),
        ("#ff9900", "Orange"),
    ]

    name = models.CharField(max_length=20, blank=False, null=False)
    description = models.TextField(max_length=250, blank=True, null=True)
    color = models.CharField(max_length=15, choices=COLORS, blank=True, null=True, default="#007fff")
    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)


class IngredientItem(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    details = models.TextField(max_length=250, blank=True, null=True)
    selected = models.BooleanField(null=False, default=False)
    customizable = models.BooleanField(null=False, default=False)
    extra_price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True
    )
    virtualshop = models.ForeignKey(VirtualShop,
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL,
                                    related_name="ingredients")
    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)

    def validate_unique(self, exclude=None):
        if IngredientItem.objects.filter(name=self.name, virtualshop=self.virtualshop).exists():
            raise ValidationError("Name must be unique per Virtual Shop")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(IngredientItem, self).save(*args, **kwargs)
        # self.foodItem.id

        # if qs.filter(foodItem__id=self.zone__site).exists():
        #     raise ValidationError('Name must be unique per site')

    # class Meta:
    #     unique_together = ("name", "")


class FoodItem(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=250, blank=True, null=True)
    foodItemCategory = models.ForeignKey(
        FoodItemCategory,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="foodItems"
    )
    virtualShop = models.ForeignKey(
        VirtualShop,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="foodItems",
        default=None
    )

    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True
    )
    ingredients = models.ManyToManyField(IngredientItem, through='IngredientChosenToFoodItem', related_name="foodItems")
    tags = models.ManyToManyField(TagFoodItem, null=True, blank=True, related_name="foodItems")

    image = models.ForeignKey(
        Image,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="foodItems"
    )

    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)

    def __repr__(self):
        return f"<FoodItem: {self.title}>"

    def __str__(self):
        return self.title


class FoodItemOption(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)

    description = models.TextField(max_length=250, blank=False, null=False)

    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=True,
        null=True
    )

    foodItem = models.ForeignKey(
        FoodItem,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name="foodItemOption"
    )

    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)

    def __repr__(self):
        return f"<FoodItemOption: {self.title}>"

    def __str__(self):
        return self.title


class IngredientChosenToFoodItem(models.Model):
    """
    Table created to intermediate FoodItem and IngredientItem in a Many-To-Many relationship
    """
    foodItem = models.ForeignKey(
        FoodItem,
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )
    ingredientItem = models.ForeignKey(
        IngredientItem,
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )
    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)


class Weekdays(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)

    def __repr__(self):
        return f"<Weekdays: {self.name}>"

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ["name"]


class OpeningHour(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    virtualShop = models.ForeignKey(
        VirtualShop,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="opening_hours"
    )

    weekDay = models.ForeignKey(
        Weekdays,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="opening_hours"
    )

    startTime = models.TimeField(null=False, blank=False)
    endTime = models.TimeField(null=False, blank=False)
    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)

    def __repr__(self):
        return f"<OpeningHour: StartTime: {self.startTime} - EndTime: {self.endTime}>"

    def __str__(self):
        return self.name
