from ..models.supplier import Supplier
from ..models.product import Product
from ..models.invoice import Invoice
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

def get_all_suppliers():
    return Supplier.objects.all()

def get_supplier_by_id(supplier_id):
    return Supplier.objects.get(id=supplier_id)

def create_supplier(data):
    supplier = Supplier.objects.create(**data)
    return supplier

def update_supplier(supplier_id, data):
    supplier = Supplier.objects.get(id=supplier_id)

    for field, value in data.items():
        setattr(supplier, field, value)

    supplier.save()
    return supplier

def delete_supplier(supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)
    supplier.delete()
    return True

def get_supplier_orders(supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)
    return supplier.orders.all()

def get_supplier_products(supplier_id):
    try:
        supplier = Supplier.objects.get(id=supplier_id)
    except ObjectDoesNotExist:
        raise ValueError("Supplier does not exist.")

    return Product.objects.filter(supplier=supplier)

def get_supplier_invoices(supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)
    return Invoice.objects.filter(supplier=supplier)

def search_suppliers(name=None, email=None, tax_id=None):
    filters = Q()

    # Filter using Django lookups to perform queries on models
    if name:
        filters |= Q(name__icontains=name)
    if email:
        filters |= Q(email__icontains=email)
    if tax_id:
        filters |= Q(tax_id__icontains=tax_id)
    
    return Supplier.objects.filter(filters)