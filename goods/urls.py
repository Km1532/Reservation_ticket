from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('category/<slug:category_slug>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
    path('catalog/product/<slug:product_slug>/', views.catalog_product, name='catalog_product'),
]
