from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="dashboard"),
    path("", include("django.contrib.auth.urls")),  # login/logout/password-change
    path("register/", views.register, name="register"),
    path("complete-profile/<int:pk>/", views.register_profile, name="register_profile"),
]