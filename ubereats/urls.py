from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('create_order', views.create_order, name="Create_Order"),
    path('dispatch_store/<int:pk>',
         views.dispatch_store_to_order, name="Dispatch_Store"),
    path("dispatch_driver/<int:pk>",
         views.dispatch_driver_to_order, name="Dispatch_Driver"),
]
