from django.urls import path
from .views import *
urlpatterns = [
        path('', home),
        path('customers/create', addCustomer),
        path('customers/', getCustomers),
        path('orders/create',addOrder),
        path('orders/', getOrders),
        path('orders/<int:pk>',getOrderByID),
        path('items/create', addItem),
        path('items/<int:pk>',updateItem)
]