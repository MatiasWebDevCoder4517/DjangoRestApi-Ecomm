from django.urls import path
from .views import ListCategory, DetailCategory, ListAccount, DetailAccount, ListProduct, DetailProduct, ListUserProfile, DetailUserProfile, ListCart, DetailCart, ListCartItem, DetailCartItem, ListPayment, DetailPayment, ListOrder, DetailOrder, ListOrderProduct, DetailOrderProduct, ListVariation, DetailVariation

urlpatterns = [
    path('categories', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),

    path('accounts', ListAccount.as_view(), name='accounts'),
    path('accounts/<int:pk>/', DetailAccount.as_view(), name='singleaccount'),

    path('products', ListProduct.as_view(), name='products'),
    path('products/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),

    path('users', ListUserProfile.as_view(), name='users'),
    path('users/<int:pk>/', DetailUserProfile.as_view(), name='singleuser'),

    path('carts', ListCart.as_view(), name='allcarts'),
    path('carts/<int:pk>', DetailCart.as_view(), name='cartdetail'),

    ##--------------------------------##
    path('payments', ListPayment.as_view(), name='payments'),
    path('payments/<int:pk>/', DetailPayment.as_view(), name='singlepayment'),

    path('orders', ListOrder.as_view(), name='orders'),
    path('orders/<int:pk>/', DetailOrder.as_view(), name='singleorder'),

    path('orderproduct', ListOrderProduct.as_view(), name='orderproduct'),
    path('orderproducts/<int:pk>/', DetailOrderProduct.as_view(),
         name='singleorderproduct'),

    path('users', ListUserProfile.as_view(), name='users'),
    path('users/<int:pk>/', DetailUserProfile.as_view(), name='singleuser'),

    path('variations', ListVariation.as_view(), name='allvariations'),
    path('variations/<int:pk>', DetailVariation.as_view(), name='variationdetail'),







]
