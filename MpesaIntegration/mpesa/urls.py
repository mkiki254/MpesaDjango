from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.payment_index, name="payment"),
]