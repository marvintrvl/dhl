# core/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from .utils import generate_qr_code

@receiver(post_save, sender=Order)
def generate_qr_code_for_package(sender, instance, created, **kwargs):
    if created:
        package = instance.package
        qr_code_image = generate_qr_code(package.id)
        package.qr_code.save(qr_code_image.name, qr_code_image)
        package.save()
