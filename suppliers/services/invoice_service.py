from ..models.invoice import Invoice

def get_all_invoices():
    return Invoice.objects.all()

def get_invoice_by_id(invoice_id):
    return Invoice.objects.get(id=invoice_id)

def create_invoice(data):
    invoice = Invoice.objects.create(**data)
    return invoice

def update_invoice(invoice_id, data):
    invoice = Invoice.objects.get(id=invoice_id)

    for field, value in data.items():
        setattr(invoice, field, value)

    invoice.save()
    return invoice

def delete_invoice(invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    invoice.delete()
    return True

def get_invoice_orders(invoice_id):
    invoice = Invoice.objects.get(id=invoice_id)
    return invoice.orders.all()