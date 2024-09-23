from django.db import models
from django.core.validators import EmailValidator


class Supplier(models.Model):
    name = models.CharField(max_length=255, null=False)
    contact_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=False, validators=[EmailValidator()])
    phone_number = models.CharField(max_length=20)
    address = models.TextField(null=False)
    tax_id = models.CharField(max_length=50)

    def __str__(self):
        return self.name