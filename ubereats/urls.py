from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('create_order', views.create_order, name="Create_Order"),
    path('detail_order/<int:pk>', views.detail_order, name="Detail_Order"),
    path('update_order/<int:pk>', views.update_order, name="Update_Order"),
    path('delete_order/<int:pk>', views.delete_order, name="Delete_Order"),
    path('dispatch_store/<int:pk>',
         views.dispatch_store_to_order, name="Dispatch_Store"),
    path("dispatch_driver/<int:pk>",
         views.dispatch_driver_to_order, name="Dispatch_Driver"),
]
