from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
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

def reviews(request):
    reviews = Review.objects.all()
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  
            review.save()
            return redirect('main:reviews')

    context = {'reviews': reviews, 'form': form}
    return render(request, 'main/reviews.html', context)