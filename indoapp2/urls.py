from django.urls import path
from indoapp2 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('/', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('order/', views.order, name='order'),
    path('cart_quan/', views.cart_quan, name='cart_quan'),
    path('remove_cart/', views.remove_cart, name='remove_cart'),
    path('placeorder/', views.placeorder, name='placeorder'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    # path('trys/', views.trys, name='trys'),
    path('products/<str:type>/', views.products, name='products'),
    path('productdetail/<int:id>/', views.product_detail, name='productdetail'),
    path('addprofile/', views.add_profile, name='addprofile'),
    path('showaddress/', views.showaddress, name='showaddress'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)