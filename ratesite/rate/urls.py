from django.urls import path

from . import views

urlpatterns = [
    path("", views.exchange_rate, name="exchange_rate"),
]