from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Account, UserProfile, Category, Product, Variation, ReviewRating, ProductGallery, Like, Cart, CartItem, Payment, Order, OrderProduct
from .serializers import RegistrationSerializer, CategorySerializer, AccountSerializer, ProductSerializer, UserProfileSerializer, CartSerializer, CartItemSerializer, PaymentSerializer, OrderSerializer, OrderProductSerializer, VariationSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import uuid


class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception = True)
        # serializer.save()
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",

                "User": serializer.data}, status=status.HTTP_201_CREATED
            )

        return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)


class ListCategory(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListAccount(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class DetailAccount(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class ListProduct(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListCart(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class DetailCart(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class ListPayment(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class DetailPayment(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class ListUserProfile(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class DetailUserProfile(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ListOrder(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DetailOrder(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ListOrderProduct(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class DetailOrderProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class ListVariation(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer


class DetailVariation(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer


class ListCartItem(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class DetailCartItem(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
