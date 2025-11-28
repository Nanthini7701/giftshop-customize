from django.shortcuts import render, redirect
from .models import Category
from django.contrib.auth import logout
from .models import Product, Wishlist, Cart
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Order
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, logout as django_logout
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse


def home(request):
    categories = Category.objects.all()
    return render(request, "base.html", {"categories": categories})
def home(request):
    faq_list = [
        ("1. What types of gifts do you offer?",
         "We offer a wide range of gifts for birthdays, anniversaries, weddings, and more."),

        ("2. Do you offer gift wrapping or personalized messages?",
         "Yes! We offer free gift wrapping and custom messages."),

        ("3. How long does delivery take?",
         "Standard shipping takes 3–7 days, express takes 1–3 days.")
    ]

    return render(request, "shop/home.html", {"faq_list": faq_list})
def enquiry(request):
    return render(request, "shop/enquiry.html")
def order_page(request):
    return render(request, 'shop/order.html')
def traking_page(request):
    return render(request, 'shop/traking.html')
def billing_page(request):
    return render(request, 'shop/billing.html')
def payment_page(request):
    return render(request, 'shop/payment.html')
def orders_page(request):
    return render(request, 'shop/ordertraking.html')
def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'shop/order_detail.html', {'order': order})
def myaccount_page(request):
    return render(request, 'shop/myaccount.html')
def password_page(request):
    return render(request, 'shop/password.html')
def categories(request):
    products = Product.objects.all()

    # Apply Filters
    occasion = request.GET.get('occasion')
    gift_type = request.GET.get('gift_type')
    price_type = request.GET.get('price_type')
    delivery = request.GET.get('delivery')

    if occasion:
        products = products.filter(occasion=occasion)
    if gift_type:
        products = products.filter(gift_type=gift_type)
    if price_type:
        products = products.filter(price_type=price_type)
    if delivery:
        products = products.filter(delivery_type=delivery)

    wishlist_count = 0
    cart_count = 0

    if request.user.is_authenticated:
        wishlist_count = Wishlist.objects.filter(user=request.user).count()
        cart_count = Cart.objects.filter(user=request.user).count()

    context = {
        "products": products,
        "wishlist_count": wishlist_count,
        "cart_count": cart_count,
    }
    return render(request, "shop/categories.html", context)

@login_required
def order_track(request, order_id):
    # If you have an Order model, load it. If not, the template shows defaults.
    try:
        from .models import Order, OrderItem
        order = get_object_or_404(Order, pk=order_id)
        order_items = OrderItem.objects.filter(order=order)
    except Exception:
        order = None
        order_items = []
    return render(request, 'shop/tracking.html', {'order': order, 'order_items': order_items})
def download_invoice(request, order_id):
    # Dummy PDF content
    content = "Invoice for order ID: {}".format(order_id)

    response = HttpResponse(content, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{order_id}.pdf"'
    return response

def wishlist(request):
    context = {
        "wishlist_count": 1,
        "cart_count": 0,
    }
   
    return render(request, "shop/wishlist.html", context)
def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "login required"})

    obj, created = Cart.objects.get_or_create(user=request.user, product_id=product_id)

    if not created:
        obj.quantity += 1
        obj.save()

    count = Cart.objects.filter(user=request.user).count()
    return JsonResponse({"count": count})
def categories_page(request):
    return render(request, "categories.html")
def gallery_page(request):
    return render(request, "gallery.html")

def blog_page(request):
    return render(request, "blogs.html")

def contact_page(request):
    return render(request, "contact.html")

def about_page(request):
    return render(request, "about.html")

def search_products(request):
    return render(request, "search.html")

def account_info(request):
    return render(request, "account.html")

def my_order(request):
    return render(request, "orders.html")

def tracking(request):
    return render(request, "tracking.html")

def password_manager(request):
    return render(request, "password.html")

def logout_page(request):
    return render(request, 'shop/logout.html')


def cart_page(request):
    return render(request, "cart.html")

def notifications_page(request):
    return render(request, "notifications.html")
@login_required
def password_page(request):
    """
    Renders the password manager page and handles password change using Django's PasswordChangeForm.
    """
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # Keep the user logged in after password change
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was updated successfully.")
            return redirect('account:password_manager')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PasswordChangeForm(user=request.user)

    context = {
        'form': form
    }
    return render(request, 'shop/password.html', context)


@login_required
def logout_page(request):
    """
    Shows the logout confirmation page. The actual logout is performed in 'perform_logout' view.
    """
    return render(request, 'shop/logout.html')


@login_required
def perform_logout(request):
    """
    POST endpoint to log the user out.
    """
    if request.method == 'POST':
        django_logout(request)
        messages.success(request, "You have been logged out.")
        return redirect('home')  # or wherever you want to send after logout
    return redirect('account:logout_confirm')