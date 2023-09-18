from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics,viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from . import models,serializers
from django.contrib.auth.models import User


def index(req):
    return render(req,'index.html',{})

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = serializers.UserSerializer
   permission_classes = [IsAuthenticated]

class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [IsAuthenticated]