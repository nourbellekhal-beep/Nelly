from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:pk>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('detail/', views.CartDetailsView.as_view(), name='cart_detail'),
    path('item/delete/<int:pk>/', views.CartItemDeleteView.as_view(), name='cart_item_delete'),
    path('item/update/<int:pk>/', views.CartItemUpdateView.as_view(), name='cart_item_update'),
]
