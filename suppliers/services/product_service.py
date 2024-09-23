from ..models.product import Product

def get_all_products():
    return Product.objects.all()

def get_product_by_id(product_id):
    return Product.objects.get(id=product_id)

def create_product(data):
    product = Product.objects.create(**data)
    return product

def update_product(product_id, data):
    product = Product.objects.get(id=product_id)

    for field, value in data.items():
        setattr(product, field, value)

    product.save()
    return product

def delete_product(product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return True