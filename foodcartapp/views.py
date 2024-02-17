import json

from django.http import JsonResponse
from django.shortcuts import render

from foodcartapp.models import Order, Cake, Level, Topping, Berries, Decor, \
    Form, Words


# Create your views here.


def lk_order(request):
    return render(request, 'lk-order.html')


def index(request):
    if request.method == 'GET':
        levels = request.GET.get('LEVELS')
        forms = request.GET.get('FORM')
        toppings = request.GET.get('TOPPING')
        berriess = request.GET.get('BERRIES')
        decors = request.GET.get('DECOR')
        wordss = request.GET.get('WORDS')
        comments = request.GET.get('COMMENTS')
        name = request.GET.get('NAME')
        phone = request.GET.get('PHONE')
        email = request.GET.get('EMAIL')
        address = request.GET.get('ADDRESS')
        date = request.GET.get('DATE')
        time = request.GET.get('TIME')
        delivery_comments = request.GET.get('DELIVCOMMENTS')

        order = Order.objects.get_or_create(name=name)
        level = Level.objects.get_or_create(level=levels)
        form = Form.objects.get_or_create(form=forms)
        topping = Topping.objects.get_or_create(topping=toppings)
        berries = Berries.objects.get_or_create(berries=berriess)
        decor = Decor.objects.get_or_create(decor=decors)
        words = Words.objects.get_or_create(words=wordss)
        Cake.objects.create(
            comment=comments,
            order=order,
            level=level,
            form=form,
            topping=topping,
            berries=berries,
            decor=decor,
            words=words
        )

        return render(request, 'index.html')
    else:
        return JsonResponse({
            'error': 'Method not allowed',
        })



def lk(request):
    return render(request, 'lk.html')

