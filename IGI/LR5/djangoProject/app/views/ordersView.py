from django.shortcuts import render,redirect
from app.models_app.salesModel import Sales
from django.views import View

from django.shortcuts import render


def orders(request):
    orders = Sales.objects.all()
    return render(request, 'orders.html', {'orders': orders})