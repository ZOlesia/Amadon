# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'sum' not in request.session:
        request.session['sum'] = 0
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, 'products/index.html')

def buy(request):
    product =str(request.POST['product']) 
    quantity = int(request.POST['quantity'])
    product_list = [['tshirt', 19.99],['sweater', 29.99],['cup', 4.99],['book', 49.99]]
    for i in range (0, len(product_list)):
        if product == product_list[i][0]:
            request.session['total'] = product_list[i][1] * quantity
            request.session['sum'] += request.session['total']
            request.session['count'] += 1


    return redirect(checkout)

def checkout(request):
    return render(request, 'products/checkout.html')