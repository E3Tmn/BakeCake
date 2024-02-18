import json
from urllib.parse import parse_qs

from django.http import JsonResponse
from django.shortcuts import render

from foodcartapp.models import Order, Cake, Level, Topping, Berries, Decor, \
    Form, Words


# Create your views here.


def lk_order(request):
    return render(request, 'lk-order.html')


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        data_str = request.body.decode('utf-8')
        data_dict = parse_qs(data_str)
        print(data_dict)
        order = Order.objects.create(
            name=data_dict['NAME'][0],
            phone=data_dict['PHONE'][0],
            email=data_dict['EMAIL'][0],
            address=data_dict['ADDRESS'][0],
            date=data_dict['DATE'][0],
            time=data_dict['TIME'][0],
        )
        if 'DELIVCOMMENTS' in data_dict:
            order.delivery_comments = data_dict['DELIVCOMMENTS'][0]
            order.save()
        level, created = Level.objects.get_or_create(level=data_dict['LEVELS'][0])
        form, created = Form.objects.get_or_create(form=data_dict['FORM'][0])
        topping, created = Topping.objects.get_or_create(topping=data_dict['TOPPING'][0])
        berries, created = Berries.objects.get_or_create(berries=data_dict['BERRIES'][0])
        decor, created = Decor.objects.get_or_create(decor=data_dict['DECOR'][0])
        cake = Cake.objects.create(
            order=order,
            level=level,
            form=form,
            topping=topping,
            berries=berries,
            decor=decor
        )
        if 'WORDS' in data_dict:
            words, created = Words.objects.get_or_create(words=data_dict['WORDS'][0])
            cake.words = words
            cake.save()
        if 'COMMENTS' in data_dict:
            cake.comment = data_dict['COMMENTS'][0]
            cake.save()

        return render(request, 'index.html')
    else:
        return JsonResponse({
            'error': 'Method not allowed',
        })


def lk(request):
    return render(request, 'lk.html')

