from django.urls import path


from .views.product.product_create_view import ProductCreateView

from .views.supplier.supplier_detail_view import SupplierDetailView
from .views.supplier.supplier_list_view import SupplierListView
from .views.supplier.supplier_search_view import SupplierSearchView
from .views.supplier.supplier_products import SupplierProductsView

urlpatterns = [
    path('suppliers/', SupplierListView.as_view(), name='supplier-list'),
    path('suppliers/<int:supplier_id>/', SupplierDetailView.as_view(), name='supplier-detail'),
    path('suppliers/search/', SupplierSearchView.as_view(), name='supplier-search'),
    path('suppliers/<int:supplier_id>/products/', SupplierProductsView.as_view(), name='supplier-products'),
    path('products/', ProductCreateView.as_view(), name='create_product'),
]