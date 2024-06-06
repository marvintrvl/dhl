from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class Customer(AbstractUser):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    last_login = None

class Business(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

class Package(models.Model):
    PACKAGE_STATUS_CHOICES = [
        ('IN_TRANSIT', 'In Transit'),
        ('DELIVERED', 'Delivered'),
        ('RETURNED', 'Returned'),
        ('EMPTY', 'Empty'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(Business, related_name='sent_packages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(Customer, related_name='received_packages', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=PACKAGE_STATUS_CHOICES, default='IN_TRANSIT')
    gps_tracking_code = models.CharField(max_length=100)
    deposit_paid = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    order_id = models.CharField(max_length=100, unique=True)
    package = models.OneToOneField(Package, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    details = models.JSONField()