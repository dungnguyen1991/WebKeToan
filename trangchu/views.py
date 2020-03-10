from django.shortcuts import render
from .models import Menu

# Create your views here.
def create_menu(node):
    items = Menu.objects.filter(menu_parent = node).order_by("menu_order")
    main_menu = []
    for item in items:
        main_menu.append({
            "item":item,
            "children": create_menu(item),
        })
    return main_menu

def index(request):
    return render(request, 'index.html', {"main_menu": create_menu(None)})