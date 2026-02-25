import razorpay
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()

            # ✅ Calculate total BEFORE clearing cart
            total_amount = int(cart.get_total_price() * 100)

            # ✅ Save Order Items
            for item in cart:
                order.items.create(
                    plant=item['plant'],
                    price=item['price'],
                    quantity=item['quantity']
                )

            # ================= COD =================
            if order.payment_method == 'COD':
                cart.clear()
                return render(request, 'orders/order_created.html', {'order': order})

            # ================= RAZORPAY =================
            elif order.payment_method == 'RAZORPAY':
                client = razorpay.Client(
                    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
                )

                payment = client.order.create({
                    "amount": total_amount,
                    "currency": "INR",
                    "payment_capture": "1"
                })

                # Save Razorpay order ID
                order.razorpay_order_id = payment['id']
                order.save()

                return render(request, 'orders/razorpay_payment.html', {
                    'order': order,
                    'razorpay_key': settings.RAZORPAY_KEY_ID,
                    'razorpay_order_id': payment['id'],
                    'total_amount': total_amount,
                })

    else:
        form = OrderCreateForm()

    return render(request, 'orders/order_create.html', {
        'form': form,
        'cart': cart
    })



def payment_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.paid = True
    order.save()

    # clear cart after payment
    cart = Cart(request)
    cart.clear()

    return render(request, 'orders/order_created.html', {'order': order})




def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})


from django.shortcuts import render
from .models import Order

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})