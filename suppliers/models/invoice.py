from django.db import models
from suppliers.models.order import Order


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50)
    invoice_date = models.DateField()
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(Order, related_name='invoices', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('overdue', 'Overdue')
    ])

    def __str__(self):
        return f"Invoice {self.invoice_number}"