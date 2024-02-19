import json
from urllib.parse import parse_qs

from django.http import JsonResponse
from django.shortcuts import render

from foodcartapp.models import Order, Cake, Level, Topping, Berries, Decor, \
    Form, Words, Account


# Create your views here.


def lk_order(request):
    return render(request, 'lk-order.html')


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        data_str = request.body.decode('utf-8')
        data_dict = parse_qs(data_str)
        if 'REG' in data_dict:
            account, created = Account.objects.get_or_create(
                phone=data_dict['REG'][0]
            )
            request.session['logged_in_user'] = account.phone
        else:
            order = Order.objects.create(
                name=data_dict['NAME'][0],
                phone=data_dict['PHONE'][0],
                email=data_dict['EMAIL'][0],
                address=data_dict['ADDRESS'][0],
                date=data_dict['DATE'][0],
                time=data_dict['TIME'][0],
            )
            account_phone = request.session.get('logged_in_user')

            if account_phone:
                account = Account.objects.get(phone=account_phone)
                order.owner = account
                order.save()
            if 'DELIVCOMMENTS' in data_dict:
                order.delivery_comments = data_dict['DELIVCOMMENTS'][0]
                order.save()
            Levels_list = ['не выбрано', '1', '2', '3']
            Forms_list = ['не выбрано', 'Круг', 'Квадрат', 'Прямоугольник']
            Toppings_list = ['не выбрано', 'Без', 'Белый соус', 'Карамельный', 'Кленовый', 'Черничный', 'Молочный шоколад', 'Клубничный']
            Berries_list = ['нет', 'Ежевика', 'Малина', 'Голубика', 'Клубника']
            Decors_list = ['нет', 'Фисташки', 'Безе', 'Фундук', 'Пекан', 'Маршмеллоу', 'Марципан']

            level, created = Level.objects.get_or_create(level=Levels_list[int(data_dict['LEVELS'][0])])
            form, created = Form.objects.get_or_create(form=Forms_list[int(data_dict['FORM'][0])])
            topping, created = Topping.objects.get_or_create(topping=Toppings_list[int(data_dict['TOPPING'][0])])
            cake = Cake.objects.create(
                order=order,
                level=level,
                form=form,
                topping=topping,
            )
            if 'BERRIES' in data_dict:
                berries, created = Berries.objects.get_or_create(berries=Berries_list[int(data_dict['BERRIES'][0])])
                cake.berries = berries
                cake.save()
            if 'DECOR' in data_dict:
                decor, created = Decor.objects.get_or_create(decor=Decors_list[int(data_dict['DECOR'][0])])
                cake.decor = decor
                cake.save()
            if 'WORDS' in data_dict:
                words, created = Words.objects.get_or_create(words=data_dict['WORDS'][0])
                cake.words = words
                cake.save()
            if 'COMMENTS' in data_dict:
                cake.comment = data_dict['COMMENTS'][0]
                cake.save()
            request.session['logged_name'] = data_dict['NAME'][0]
            request.session['logged_email'] = data_dict['EMAIL'][0]
        return render(
            request,
            'index.html',
        )
    else:
        return JsonResponse({
            'error': 'Method not allowed',
        })


def lk(request):
    account_phone = request.session.get('logged_in_user')
    context = {}
    if account_phone:
        account = Account.objects.get(phone=account_phone)
        for order in account.orders.all():
            order.update_status_if_delivered()
            order.sum_cost()
        context['account'] = account
    if context:
        return render(request, 'lk.html', context)
    else:
        return render(request, 'lk.html')

