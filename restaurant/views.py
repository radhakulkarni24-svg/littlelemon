from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


# Template views
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def menu(request):
    menu_items = Menu.objects.all()
    return render(request, "menu.html", {"menu": menu_items})


def menu_item(request, pk):
    item = get_object_or_404(Menu, pk=pk)
    return render(request, "menu_item.html", {"item": item})


def book(request):
    return render(request, "book.html")


# API viewsets
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
