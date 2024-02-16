from django.shortcuts import render

# Create your views here.


def lk_order(request):
    return render(request, 'lk-order.html')


def index(request):
    DATA = {
        'Levels': {
            'num1': '1',
            'num2': '2',
            'num3': '3'
        },
        'Forms': {
            'form1': 'Круг',
            'form2': 'Квадрат',
            'form3': 'Прямоугольник'
        },
        'Toppings': {
            'topping1': 'Без',
            'topping2': 'Белый соус',
            'topping3': 'Карамельный',
            'topping4': 'Кленовый',
            'topping5': 'Черничный',
            'topping6': 'Молочный шоколад',
            'topping7': 'Клубничный'
        },
        'Berries': {
            'berries1': 'Ежевика',
            'berries2': 'Малина',
            'berries3': 'Голубика',
            'berries4': 'Клубника'
        },
        'Decors': {
            'decor1': 'Фисташки',
            'decor2': 'Безе',
            'decor3': 'Фундук',
            'decor4': 'Пекан',
            'decor5': 'Маршмеллоу',
            'decor6': 'Марципан',


        },
        'Words': 'С днем рождения!'
    }
    return render(request, 'index.html', {'DATA': DATA})


def lk(request):
    return render(request, 'lk.html')

