from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Order, _get_all_order
from .forms import DriverModelForm, OrderModelForm, StoreModelForm


def index(request):
    orders = _get_all_order()

    for order in orders:
        if order.is_store_completed and order.is_driver_completed:
            order.is_completed = True
            order.save()

    context = {
        'orders': orders
    }

    return render(request, 'index.html', context)


def create_order(request):
    order_form = OrderModelForm()

    if request.method == 'POST':
        order_form = OrderModelForm(request.POST)

        if order_form.is_valid():
            order_form.save()

        return redirect("/ubereats/")

    context = {'order_form': order_form}
    return render(request, 'create_order.html', context)


def update_order(request, pk):
    try:
        order = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        raise Http404("No OrderModel matches the given query.")

    order_form = OrderModelForm()
    store_form = StoreModelForm()
    driver_form = DriverModelForm()

    if request.method == "POST":
        order_form = OrderModelForm(request.POST, instance=order)
        store_form = StoreModelForm(request.POST, instance=order)
        driver_form = DriverModelForm(request.POST, instance=order)

        if order_form.is_valid():
            order_form.save()
            store_form.save()
            driver_form.save()

        return redirect("/ubereats/")

    context = {
        'order_form': order_form,
        'store_form': store_form,
        'driver_form': driver_form
    }
    return render(request, 'update_order.html', context)


def delete_order(request, pk):
    try:
        order = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        raise Http404("No OrderModel matches the given query.")

    if request.method == "POST":
        order.delete()
        return redirect("/ubereats/")

    context = {'order': order}
    return render(request, 'delete_order.html', context)


def dispatch_store_to_order(request, pk):
    try:
        order = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        raise Http404("No OrderModel matches the given query.")

    store_form = StoreModelForm()

    if request.method == 'POST':
        order.is_store_completed = True

        store_form = StoreModelForm(request.POST, instance=order)

        if store_form.is_valid():
            store_form.save()

        return redirect("/ubereats/")

    context = {'store_form': store_form}
    return render(request, 'dispatch_store.html', context)


def dispatch_driver_to_order(request, pk):
    try:
        order = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        raise Http404("No OrderModel matches the given query.")

    if order.is_store_completed:
        order.is_driver_completed = True
    else:
        return HttpResponse('請先等待商家餐點完成後，再發派司機')

    driver_form = DriverModelForm()

    if request.method == 'POST':
        driver_form = DriverModelForm(request.POST, instance=order)

        if driver_form.is_valid():
            driver_form.save()

        return redirect("/ubereats/")

    context = {'driver_form': driver_form}
    return render(request, 'dispatch_driver.html', context)
