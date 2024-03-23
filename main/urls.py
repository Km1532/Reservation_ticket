from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('reviews/', views.reviews, name='reviews'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('payment_delivery/', views.payment_delivery, name='payment_delivery'),  
]