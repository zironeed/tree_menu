from django.shortcuts import render
from menu_app.models import Menu


def index(request):
    menus = Menu.objects.all()
    return render(request, 'menu_app/index.html', {'menus': menus})
