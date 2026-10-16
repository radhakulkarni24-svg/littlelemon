from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"menu", views.MenuViewSet)
router.register(r"booking", views.BookingViewSet)

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("menu/", views.menu, name="menu"),
    path("menu/<int:pk>/", views.menu_item, name="menu_item"),
    path("book/", views.book, name="book"),
    path("api/", include(router.urls)),
]
