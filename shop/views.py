from django.shortcuts import render

# Create your views here.

def index(request):
    shop = [
        {'title': 'Bikes'},
        {'title': 'Parts'},
    ]
    return render(request, 'shop/index.html', {
        'show_shop': False,
        'shop': shop
    })
