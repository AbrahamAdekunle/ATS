from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=30, null=True, blank=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=19, unique=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to="user_profile_picture", default="avatar.svg")
    age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(16)], null=True, blank=True)
    phone_number = PhoneNumberField(unique=True, null=True,)
    is_vendor = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()


class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name_of_store = models.CharField(max_length=500, null=True)
    location_of_store = models.TextField()
    next_of_kin_name = models.CharField(max_length=200)
    next_of_kin_address = models.TextField()
    next_of_kin_phone_number = PhoneNumberField(unique=True)


    # def __str__(self):
        # return self.name_of_store



