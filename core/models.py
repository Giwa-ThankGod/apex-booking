from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.html import escape

from .managers import CustomerUserManager
from random import randint

def generate_booking_number():
    min = pow(10, 10-1)
    max = pow(10, 10) - 1
    return randint(min,max)

# Create your models here.
class User(AbstractUser):
    gender_choice = (
        ('Male','Male'),
        ('Female','Female'),
    )
    username = None
    email = models.EmailField(_('email address'), unique=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, choices=gender_choice)
    phone = models.CharField(max_length=20)
    dob = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    area_code = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', default="avatars/avatar.jpg",)

    is_admin = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomerUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs) -> None:
        if not self.avatar:
            self.avatar = 'avatars/avatar.jpg'
        super().save(*args, **kwargs)

    @property
    def avatarUrl(self):
        try:
            url = self.avatar.url
        except:
            url = ''
        return url


class Booking(models.Model):
    booking_number = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    client = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.booking_number

    def save(self, *args, **kwargs) -> None:
        while not self.booking_number:
            booking_number = generate_booking_number()
            object_with_similar_booking_number = Booking.objects.filter(booking_number = booking_number)
            if not object_with_similar_booking_number:
                self.booking_number = booking_number
        super().save(*args, **kwargs)

class Discount(models.Model):
    client = models.ForeignKey('User', null=False, on_delete=models.CASCADE) #To identify the client with discount.
    client_booking_number = models.CharField(max_length=10, default=None) #information admin needs to give discount.
    discount_amount = models.IntegerField(default=0, null=False)
    
    def __str__(self):
        return f'{self.client.booking_number} {self.discount_amount}'

    def save(self, *args, **kwargs) -> None:

        discounts = Discount.objects.all()
        if discounts:
            for discount in discounts:
                discount.delete()
        
        super().save(*args, **kwargs)