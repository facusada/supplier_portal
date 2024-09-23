from django.urls import path

from suppliers.views.supplier_detail_view import SupplierDetailView
from .views.supplier_list_view import SupplierListView

urlpatterns = [
    path('suppliers/', SupplierListView.as_view(), name='supplier-list'),
    path('suppliers/<int:supplier_id>/', SupplierDetailView.as_view(), name='supplier-detail'),
]