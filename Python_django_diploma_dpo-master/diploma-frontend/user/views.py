import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.db.models import QuerySet

from django.shortcuts import render
from rest_framework.generics import get_object_or_404

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Product
from user.models import Profile, Cart
from user.serializers import BasketSerializer


class UserLogoutView(LogoutView):
    """Logout"""
    reverse = '/'


class SignInView(APIView):
    """Log in"""

    def post(self, request: Request) -> Response:
        data = json.loads(list(request.POST.items())[0][0])
        user = authenticate(username=data["username"], password=data["password"])
        login(request, user)

        return Response()


class RegisterView(APIView):
    """Register"""

    def post(self, request: Request) -> Response:
        data = json.loads(list(request.POST.items())[0][0])
        user = User.objects.create_user(
            username=data["username"],
            email=f"{data['username']}@example.com",
            password=data["password"],
        )
        user.save()
        Profile.objects.create(user=user)
        login(request, user)

        return Response()

class ProfileDetailsView(APIView):
    """Profile details"""

    def get(self, request: Request) -> Response:
        profile = Profile.objects.get(user_id=request.user.id)
        profile_details = {
            "fullName": profile.fullName,
            "email": request.user.email,
            "phone": profile.phone,
            "avatar": {"src": profile.avatar_url, "alt": "Image  description"},
        }
        return Response(profile_details)

    def post(self, request: Request) -> Response:
        profile = Profile.objects.get(user_id=request.user.id)
        user = request.user

        user.email = request.data["email"]
        profile.fullName = request.data["fullName"]
        profile.phone = request.data["phone"]

        user.save()
        profile.save()

        profile_details = {
            "fullName": profile.fullName,
            "email": request.user.email,
            "phone": profile.phone,
            "avatar": {"src": profile.avatar_url, "alt": "Image description"},
        }

        return Response(profile_details)


class AvatarUpdateView(APIView):
    """Avatar update"""

    def post(self, request: Request) -> Response:
        profile = Profile.objects.get(user_id=request.user.id)
        profile.avatar = request.data["avatar"]
        profile.save()

        profile_details = {"src": profile.avatar_url, "alt": "Image description"}

        return Response(profile_details)


class PasswordUpdateView(APIView):
    """Password update"""

    def post(self, request: Request) -> Response:
        user = request.user
        if user.check_password(request.data["currentPassword"]):
            user.set_password(request.data["newPassword"])
            user.save()
            return Response(status=200)


class CartView(APIView):
    """Cart view"""

    serializer_class = BasketSerializer

    def get_queryset(self, id: int) -> QuerySet:
        queryset = Product.objects.get(id=id)
        return queryset

    def get(self, request: Request) -> Response:
        cart = Cart(request)
        items = [self.get_queryset(int(item_id)) for item_id in cart.cart.keys()]

        if not items:
            return Response(None)

        serializer = BasketSerializer(items, many=True, context=request)
        return Response(serializer.data)


class BasketView(APIView):
    """Basket view"""

    serializer_class = BasketSerializer

    def get_queryset(self, id: int) -> QuerySet:
        queryset = Product.objects.get(id=id)
        return queryset

    def get(self, request: Request) -> Response:
        cart = Cart(request)
        items = [self.get_queryset(int(item_id)) for item_id in cart.cart.keys()]

        if not items:
            return Response(None)

        serializer = BasketSerializer(items, many=True, context=request)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        data = request.data
        cart = Cart(request)
        item = get_object_or_404(Product, id=data["id"])
        cart.add(
            item,
            quantity=data["count"],
        )

        items = [self.get_queryset(int(item_id)) for item_id in cart.cart.keys()]
        if not items:
            return Response(None)
        serializer = BasketSerializer(items, many=True, context=request)
        return Response(serializer.data)

    def delete(self, request: Request) -> Response:
        cart = Cart(request)
        data = json.loads(request.body)
        item = Product.objects.get(id=data["id"])
        cart.remove(item, data["count"])

        items = [self.get_queryset(int(item_id)) for item_id in cart.cart.keys()]
        if not items:
            return Response(None)
        serializer = BasketSerializer(items, many=True, context=request)
        return Response(serializer.data)

