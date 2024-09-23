from ..models.order import Order

def get_all_orders():
    return Order.objects.all()

def get_order_by_id(order_id):
    return Order.objects.get(id=order_id)

def create_order(data):
    order = Order.objects.create(**data)
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