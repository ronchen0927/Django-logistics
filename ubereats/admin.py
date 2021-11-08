from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'food', 'drink')  # 顯示欄位


admin.site.register(Order, OrderAdmin)  # 加入至Administration(管理員後台)
