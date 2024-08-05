from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import login
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth.models import User
from django.http import JsonResponse


class RegisterViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def list(self, request):
        return render(request, "registration/register.html")

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data["password"])
            user.save()
            return JsonResponse({"success": True, "redirect_url": "/api/user/login/"})
        return JsonResponse({"success": False, "errors": serializer.errors})


class LoginViewSet(viewsets.GenericViewSet):
    serializer_class = LoginSerializer

    def list(self, request):
        return render(request, "login/login.html")

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            login(request, user)
            return JsonResponse({"success": True, "redirect_url": "admin"})
        return JsonResponse({"success": False, "errors": serializer.errors})
