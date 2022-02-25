from rest_framework import serializers
from .models import Account, UserProfile, Category, Product, Variation, ReviewRating, ProductGallery, Like, Cart, CartItem, Payment, Order, OrderProduct
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'email', 'username', 'password')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'username': ('username already exists')})

        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class VariationSerializer(serializers.ModelSerializer):

    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all())

    class Meta:

        fields = (
            'id',
            'variation_category',
            'variation_value',
            'is_active',
            'product',
            'created_date',
        )
        model = Variation


class PaymentSerializer(serializers.ModelSerializer):

    users = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Account.objects.all())

    class Meta:

        fields = (
            'id',
            'user',
            'payment_id',
            'payment_method',
            'amount_paid',
            'status',
            'created_at',

        )
        model = Payment


class OrderSerializer(serializers.ModelSerializer):

    users = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Account.objects.all())

    payments = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Payment.objects.all())

    class Meta:

        fields = (
            'id',
            'first_name',
            'last_name',
            'user',
            'order_number',
            'payment',
            'phone',
            'email',
            'address_line_1',
            'country',
            'state',
            'city',
            'order_note',
            'order_total',
            'tax',
            'status',
            'is_ordered',
            'created_at',

        )
        model = Order


class OrderProductSerializer(serializers.ModelSerializer):

    orders = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Order.objects.all())

    accounts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Account.objects.all())

    payments = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Payment.objects.all())

    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all())

    variations = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Variation.objects.all())

    class Meta:

        fields = (
            'id',
            'order',
            'payment',
            'user',
            'product',
            'variations',
            'quantity',
            'product_price',
            'ordered',
            'created_at',
            'updated_at',


        )
        model = OrderProduct


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'category_name',
            'slug',
            'description',
            'cat_image',

        )
        model = Category


class UserProfileSerializer(serializers.ModelSerializer):

    accounts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Account.objects.all())

    class Meta:
        fields = (
            'id',
            'user',
            'address_line_1',
            'address_line_2',
            'profile_picture',
            'city',
            'state',
            'country',
        )
        model = UserProfile


class ProductSerializer(serializers.ModelSerializer):

    categories = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all())

    class Meta:
        fields = (
            'id',
            'product_name',
            'slug',
            'description',
            'description1',
            'description2',
            'description3',
            'price',
            'images',
            'stock',
            'is_available',
            'category',
            'created_date',
            'modified_date',


        )
        model = Product


class AccountSerializer(serializers.ModelSerializer):

    class Meta:

        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'date_joined',
            'last_login',
            'is_admin',

        )
        model = Account


class CartItemSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Account.objects.all())
    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all())
    variations = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Variation.objects.all())

    class Meta:
        fields = ('id', 'user', 'product', 'variations',
                  'cart', 'quantity',)
        model = CartItem


class CartSerializer(serializers.ModelSerializer):

    cart_id = CartItemSerializer(read_only=True, many=False)
    accounts = AccountSerializer(read_only=True, many=True)
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        fields = ('cart_id', 'date_added', 'accounts', 'products')
        model = Cart


class ReviewRatingSerializer(serializers.ModelSerializer):

    users = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Account.objects.all())
    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all())

    class Meta:
        fields = ('id', 'subject', 'user', 'product',
                  'review', 'rating', 'status', 'created_at',)
        model = ReviewRating
