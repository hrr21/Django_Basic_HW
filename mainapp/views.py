from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    context = {
        'products': Product.objects.all(),

    }
    return render(request, 'mainapp/products.html', context=context)



def test_context(request):
    context = {
        'title': 'Добро пожаловать!',
        'username': 'Ivan Ivanov',
        'products': [
            {'name': 'Черное худи', 'price': '2 990 руб.'},
            {'name': 'Джинсы', 'price': '5 990 руб.'}
        ],

        'promotion_products': [
            {'name': 'Туфли Dr Martins', 'price': '10 000 руб.'},
        ],
    }

    return render(request, 'mainapp/context.html', context)
