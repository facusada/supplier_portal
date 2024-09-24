from ..models.order import Order
from ..models.product import Product
from ..models.supplier import Supplier


def get_all_orders():
    return Order.objects.all()

def get_order_by_id(order_id):
    return Order.objects.get(id=order_id)

def create_order(data):
    supplier_id = data.get('supplier')
    product_ids = data.get('products')

    try:
        supplier_obj = Supplier.objects.get(id=supplier_id.id)
    except Supplier.DoesNotExist:
        raise ValueError("Supplier does not exist.")

    product_ids = [product.id for product in product_ids]
    products = Product.objects.filter(id__in=product_ids)

    if products.count() != len(product_ids):
        raise ValueError("Some products do not exist.")
    
    order = Order.objects.create(
        supplier=supplier_obj,
        total_amount=data.get('total_amount')
    )
    
    order.products.set(products)
    
    return order

def update_order(order_id, data):
    order = Order.objects.get(id=order_id)

    for field, value in data.items():
        setattr(order, field, value)

    order.save()
    return order

def delete_order(order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return True

def get_order_products(order_id):
    order = Order.objects.get(id=order_id)
    return order.products.all()