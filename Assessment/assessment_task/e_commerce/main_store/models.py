from django.db import models

from nucleus.models import User, Vendor


# Create your models here.

class ActiveOrder(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_checked_out=False)


class InactiveOrder(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_checked_out=True)


class Labels(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=80, null=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Item(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=2000)
    price = models.FloatField()
    discount = models.PositiveIntegerField(null=True, blank=True, default=0,
                                           help_text="Amount to be removed from ORIGINAL PRICE"
                                           )
    description = models.TextField()
    specifications = models.TextField(null=True, blank=True)
    key_features = models.TextField(null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, blank=True, null=True, default="Official Store")
    labels = models.ManyToManyField(Labels, blank=True)
    picture_of_product_1 = models.ImageField(upload_to="product_images")
    picture_of_product_2 = models.ImageField(upload_to="product_images")
    picture_of_product_3 = models.ImageField(upload_to="product_images")
    picture_of_product_4 = models.ImageField(upload_to="product_images", blank=True)

    class Meta:
        unique_together = ("name", "description", 'vendor')

    def get_category(self):
        return self.sub_category.category

    def get_price_discount_percentage(self):
        return round((self.discount / self.price) * 100)

    def get_real_price(self):
        try:
            return abs(self.price - self.discount)
        except:
            return self.price


class OrderedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    session = models.CharField(max_length=50, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_checked_out = models.BooleanField(default=False)

    objects = models.Manager()
    active_objects = ActiveOrder()
    inactive_objects = InactiveOrder()

    class Meta:
        unique_together = ("user", "item", "quantity")

    def __str__(self):
        return self.item.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    session = models.CharField(max_length=100, blank=True)
    ordered_items = models.ManyToManyField(OrderedItem)
    date_created = models.DateTimeField(auto_now_add=True)
    is_checked_out = models.BooleanField(default=False)

    objects = models.Manager()
    active_objects = ActiveOrder()
    inactive_objects = InactiveOrder()


class WishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_items = models.ManyToManyField(Item)

    # def __str__(self):
    #     return self.items


class Feedback(models.Model):
    RATING_CHOICES = (
        ("1", "*"),
        ("2", "**"),
        ("3", "***"),
        ("4", "****"),
        ("5", "******")
    )

    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    comments = models.TextField()
    rating = models.CharField(max_length=1, choices=RATING_CHOICES, null=True, blank=True)


class Checkout(models.Model):
    DELIVERY_CHOICES = (
        ("D", "Door Delivery"),
        ("P", "Pick Up Station")
    )

    PAYMENT_CHOICES = (
        ("Pay On Delivery", "Pay On Delivery"),
        ("Pay With Card", "Pay With Card"),
        ("Credit Card", "Credit Card"),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=5000)
    delivery = models.CharField(max_length=1, choices=DELIVERY_CHOICES, null=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, null=True)
    checkout_date = models.DateTimeField(auto_now_add=True)
