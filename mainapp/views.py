from django.shortcuts import render


def index(request):
    return render(request,'mainapp/index.html')


def products(request):
    return render(request,'mainapp/products.html')

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