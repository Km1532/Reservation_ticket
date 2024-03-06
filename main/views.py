from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):


    context = {
        'title': 'Home - Головна',
        'content': "Вітаємо на  квитковому сервісі ",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - Про нас',
        'content': "Про нас",
        'text_on_page': "Ласкаво просимо до нашого магазину квитків на концерти! У нас ви знайдете найкращі квитки на найочікуваніші музичні події. Запрошуємо вас на незабутню музичну подорож, де ви зможете насолодитися живими виступами улюблених виконавців. Оберіть свій концерт, забронюйте квиток і готуйтеся до неймовірних емоцій та незабутнього враження! Долучайтесь до нас і станьте частиною музичного світу!"
    }

    return render(request, 'main/about.html', context)

def contacts(request):
    return render(request, 'main/contacts.html', {'title': 'Контакти'})

def payment_delivery(request):
    return render(request, 'main/payment_delivery.html', {'title': 'Оплата і Доставка'})