from django.urls import path
from . import views
 
app_name = "shop" 

urlpatterns = [
    path('', views.home, name='home'),
      path("enquiry/", views.enquiry, name="enquiry"),
    # Main pages
  
    path('gallery/', views.gallery_page, name="gallery"),
    path('blogs/', views.blog_page, name="blogs"),
    path('contact/', views.contact_page, name="contact"),
    path('about/', views.about_page, name="about"),
    path("categories/", views.categories, name="categories"),
   path('order/', views.order_page, name='order'),
   path('billing/', views.billing_page, name='billing'),
   path('payment/', views.payment_page, name='payment'),
   
    path("cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    # Search
    path('search/', views.search_products, name="search"),
    path("wishlist/", views.wishlist, name="wishlist"),

    # Profile & account
    path('account/', views.myaccount_page, name="myaccount"),
     path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    
   path('ordertraking/', views.orders_page, name='ordertraking'),
    path('password/', views.password_page, name='password'),
    path('logout/', views.logout_page, name='logout'),
     path('order/<int:order_id>/track/', views.order_track, name='tracking'),
    # Icons pages
     path('traking/', views.traking_page, name='traking'), 
    path('download-invoice/<int:order_id>/', views.download_invoice, name='download_invoice'),
    path('notifications/', views.notifications_page, name="notifications"),
]
