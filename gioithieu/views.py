from django.shortcuts import render
from trangchu.models import Menu
from trangchu.views import create_menu
from .models import GioiThieu
from django.shortcuts import get_object_or_404

# Create your views here.
def gioi_thieu(request):
    danh_muc = Menu.objects.filter(menu_parent=Menu.objects.get(menu_link='/gioithieu/'))
    gioithieu = get_object_or_404(GioiThieu, menu=danh_muc[0])
    return render(request, 'gioithieu/gioithieu_chitiet.html', {'gioithieu': gioithieu,
                                                                'danh_muc': danh_muc,
                                                                'main_menu': create_menu(None)})


def chi_tiet(request, gioi_thieu_id):
    danh_muc = Menu.objects.filter(menu_parent=Menu.objects.get(menu_link='/gioithieu/'))
    gioithieu = get_object_or_404(GioiThieu, menu=get_object_or_404(Menu,pk=gioi_thieu_id))
    return render(request, 'gioithieu/gioithieu_chitiet.html', {'gioithieu': gioithieu,
                                                                'danh_muc': danh_muc,
                                                                'main_menu': create_menu(None)})