from django.shortcuts import render, redirect
from django.views import View
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.utils import get_cart

class CreateOrderView(View):
    def get(self, request):
        cart = get_cart(request)
        if not cart.items.exists():
            return redirect('cart_detail')
        form = OrderCreateForm()
        return render(request, 'orders/shipping.html', {'cart': cart, 'form': form})

    def post(self, request):
        cart = get_cart(request)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.save()
            
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    service=item.service,
                    price=item.service.price,
                    quantity=item.quantity
                )
                # Update stock
                item.service.stock -= item.quantity
                item.service.save()
            
            # Clear cart
            cart.items.all().delete()
            
            return render(request, 'orders/confirmation.html', {'order': order})
        
        return render(request, 'orders/shipping.html', {'cart': cart, 'form': form})
