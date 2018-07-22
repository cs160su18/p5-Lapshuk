from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('scan/', views.scan, name='scan'),
    path('item/', views.item, name='item'),
    path('stock/', views.stock, name='stock'),
    path('item_details/', views.item_details, name='item_details'),
    path('cart/', views.cart, name='cart'),
    path('cart_details/', views.cart_details, name='cart_details'),
    path('get_user_by_id/', views.user_details_by_id, name='user_details'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('add_stock/', views.add_stock, name='add_stock'),
    # path('activity/',views.activity, name='activity'),
  
]