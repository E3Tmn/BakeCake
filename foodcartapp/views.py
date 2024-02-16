from django.shortcuts import render

# Create your views here.


def lk_order(request):
    return render(request, 'lk-order.html')


def index(request):
    return render(request, 'index.html')


def lk(request):
    return render(request, 'lk.html')

