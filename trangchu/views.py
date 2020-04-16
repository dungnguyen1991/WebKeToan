from django.shortcuts import render
from .models import Menu
from tintuc.models import TinTuc
from quydinhnghiepvu.models import QuyDinhNghiepVu
from vanban.models import VanBan
from hoidap.models import TraLoi
from tuyendung.models import TuyenDung

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
    ds_tintuc = TinTuc.objects.all().order_by('-ngay_tao')[:4]
    ds_quydinhnghiepvu = QuyDinhNghiepVu.objects.all().order_by('-pk')[:4]
    ds_tintucnoibat = TinTuc.objects.filter(tin_noi_bat=True).order_by('-ngay_tao')[:4]
    ds_tintucsaovang = TinTuc.objects.filter(menu=Menu.objects.get(pk=37)).order_by('-ngay_tao')[:4]
    ds_vanban = VanBan.objects.all().order_by('-pk')[:4]
    ds_hoidap = TraLoi.objects.all().order_by('-pk')[:7]
    ds_kinhnghiemkienthuc = TinTuc.objects.filter(menu=Menu.objects.get(pk=38)).order_by('-ngay_tao')[:3]
    ds_tuyendung = TuyenDung.objects.all().order_by('-pk')[:3]
    return render(request, 'index.html', {'main_menu': create_menu(None),
                                          'ds_tintuc': ds_tintuc,
                                          'ds_quydinhnghiepvu': ds_quydinhnghiepvu,
                                          'ds_tintucnoibat': ds_tintucnoibat,
                                          'ds_tintucsaovang': ds_tintucsaovang,
                                          'ds_vanban': ds_vanban,
                                          'ds_hoidap': ds_hoidap,
                                          'ds_kinhnghiemkienthuc': ds_kinhnghiemkienthuc,
                                          'ds_tuyendung': ds_tuyendung})