from django.db import models
import uuid
from core.models.models_account import Customer
from core.models.models_store import FoodItem, FoodItemOption
from core.models.models_regions import DeliveryAddress


class PaymentMethod(models.Model):
    type_card = [
        ("Debit", "Debit"),
        ("Credit", "Credit"),
    ]

    stripeToken = models.CharField(max_length=250, null=False, blank=False)

    type = models.CharField(
        max_length=20,
        choices=type_card,
        null=False,
        blank=False
    )
    principal = models.BooleanField(default=False)

    customer = models.ForeignKey(
        Customer,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)

    class Meta:
        verbose_name = 'Payment Method'
        verbose_name_plural = 'Payments Methods'

    def __repr__(self):
        return f"<PaymentMethod: {self.customer}"

    def __str__(self):
        return {self.customer}


class Cart(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    customer = models.ForeignKey(
        Customer,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="cart"
    )

    deliveryAddress = models.ForeignKey(
        DeliveryAddress,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="cart"
    )

    activate = models.BooleanField(blank=False, null=False, default=False)

    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)


    def __repr__(self):
        return f"<Cart: {self.uuid}>"

    def __str__(self):
        return str(self.uuid)


class OrderItem(models.Model):
    quantity = models.IntegerField(blank=False, null=False)

    foodItem = models.ForeignKey(
        FoodItem,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="orderItem"
    )

    foodItemOptions = models.ManyToManyField(
        FoodItemOption,
        null=True,
        blank=True,
        related_name="orderItem"
    )

    cart = models.ForeignKey(
        Cart,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="orderItem"
    )

    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)

    def __repr__(self):
        return f"<ID: {self.id}>"

    def __str__(self):
        return str(self.id)

    def total(self):
        return self.foodItem.price * self.quantity


class Order(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    status = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    cart = models.OneToOneField(
        Cart,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    createAt = models.DateTimeField(auto_now_add=True, auto_created=True)
    updateAt = models.DateTimeField(auto_now=True, auto_created=True)

    def __repr__(self):
        return f"<UUID: {self.uuid}>"

    def __str__(self):
        return str(self.uuid)
