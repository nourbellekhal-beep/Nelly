from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from services.models import Service
from .models import Cart, CartItem
from .utils import get_cart

class AddToCartView(View):
    def post(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity > service.stock:
            messages.error(request, f"Désolé, seulement {service.stock} unités disponibles.")
            return redirect('service_detail', pk=pk)
        
        cart = get_cart(request)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, service=service)
        
        if not created:
            if cart_item.quantity + quantity > service.stock:
                 messages.error(request, f"Désolé, seulement {service.stock} unités au total peuvent être commandées.")
                 return redirect('service_detail', pk=pk)
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
            
        cart_item.save()
        messages.success(request, f"{service.name} ajouté au panier.")
        return redirect('cart_detail')

class CartDetailsView(DetailView):
    model = Cart
    template_name = 'cart/detail_cart.html'
    context_object_name = 'cart'

    def get_object(self, queryset=None):
        return get_cart(self.request)

class CartItemDeleteView(DeleteView):
    model = CartItem
    template_name = 'cart/cartitem_confirm_delete.html'
    success_url = reverse_lazy('cart_detail')

    def get_queryset(self):
        cart = get_cart(self.request)
        return CartItem.objects.filter(cart=cart)

class CartItemUpdateView(View):
    def post(self, request, pk):
        cart = get_cart(request)
        cart_item = get_object_or_404(CartItem, pk=pk, cart=cart)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity > cart_item.service.stock:
             messages.error(request, f"Désolé, seulement {cart_item.service.stock} unités disponibles.")
        else:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, "Quantité mise à jour.")
            
        return redirect('cart_detail')
