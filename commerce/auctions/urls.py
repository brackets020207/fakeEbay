from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("sell", views.create_listing, name = "list"),
    path("categories", views.category_menu, name = "categories"),
    path("categories/<str:category_cd>", views.view_category, name = "category"),
    path("listing/<int:listing_id>", views.view_listing, name = "listing")
]
