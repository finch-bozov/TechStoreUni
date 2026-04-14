from django.shortcuts import render
from store.models import Product
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

# Home Page
def home(request):
    category = request.GET.get('category')
    search = request.GET.get('search')

    products = Product.objects.all()

    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())

    if category:
        products = products.filter(category=category)

    if search:
        products = products.filter(name__icontains=search)

    return render(request, 'store/home.html', {
        'products': products,
        'cart_count': cart_count
    })

# Product Details
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/product_detail.html', {'product': product})

# Cart
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    # out of stock
    if product.stock <= 0:
        messages.error(request, "This product is out of stock.")
        return redirect(request.META.get('HTTP_REFERER', 'home'))

    cart = request.session.get('cart', {})

    current_qty = cart.get(str(id), 0)

    # exceeding stock
    if current_qty >= product.stock:
        return redirect('cart')

    if product.stock <= 0:
        messages.error(request, "Product is out of stock")
        return redirect('cart')


    cart[str(id)] = current_qty + 1
    request.session['cart'] = cart

    return redirect('cart')

def cart_view(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            continue
        product.quantity = quantity
        product.total_price = product.price * quantity
        total += product.total_price
        products.append(product)

    return render(request, 'store/cart.html', {
        'products': products,
        'total': total
    })

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        del cart[str(id)]

    request.session['cart'] = cart
    return redirect('cart')

# Checkout
def checkout(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('cart')

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)

        if product.stock < quantity:
            return redirect('cart')

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        product.stock -= quantity
        product.save()

    request.session['cart'] = {}

    return render(request, 'store/checkout_success.html')

# Increase quantity for item to buy
def increase_qty(request, id):
    cart = request.session.get('cart', {})

    product = Product.objects.get(id=id)
    current_qty = cart.get(str(id), 0)

    if current_qty < product.stock:
        cart[str(id)] = current_qty + 1

    request.session['cart'] = cart
    return redirect('cart')

# Decrease quantity for item to buy
def decrease_qty(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)] -= 1

        if cart[str(id)] <= 0:
            del cart[str(id)]

    request.session['cart'] = cart
    return redirect('cart')

# Remove one item from cart
def remove_item(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        del cart[str(id)]

    request.session['cart'] = cart
    return redirect('cart')

# Remove all items from cart
def clear_cart(request):
    request.session['cart'] = {}
    return redirect('cart')