from django.shortcuts import render, get_object_or_404
from trangchu.views import create_menu
from trangchu.models import Menu
from tintuc.views import phan_trang
from .models import TuyenDung
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def tuyen_dung(request):
    muc_tuyen_dung = Menu.objects.filter(menu_parent = Menu.objects.get(menu_link = '/tuyendung/'))
    list_tuyen_dung = TuyenDung.objects.filter(menu = muc_tuyen_dung[0])
    
    # get trang hien tai
    page = request.GET.get('page', 1)

    # so trang
    paginator = Paginator(list_tuyen_dung, 2)
    
    try:
        tuyendungs = paginator.page(page)
    except PageNotAnInteger:
        tuyendungs = paginator.page(1)
    except EmptyPage:
        tuyendungs = paginator.page(paginator.num_pages)

    return render(request, 'tuyendung/tuyendung_main.html', {'main_menu': create_menu(None),
                                                             'muc_tuyen_dung': muc_tuyen_dung,
                                                             'tuyendungs': tuyendungs,
                                                             'xu_ly_phan_trang':phan_trang(tuyendungs.number, tuyendungs.paginator.num_pages, 2),})

def danh_muc_tuyen_dung(request, danh_muc_id):
    muc_tuyen_dung = Menu.objects.filter(menu_parent = Menu.objects.get(menu_link = '/tuyendung/'))
    list_tuyen_dung = TuyenDung.objects.filter(menu = get_object_or_404(Menu, pk=danh_muc_id))
    
    # get trang hien tai
    page = request.GET.get('page', 1)

    # so trang
    paginator = Paginator(list_tuyen_dung, 2)
    
    try:
        tuyendungs = paginator.page(page)
    except PageNotAnInteger:
        tuyendungs = paginator.page(1)
    except EmptyPage:
        tuyendungs = paginator.page(paginator.num_pages)

    return render(request, 'tuyendung/tuyendung_main.html', {'main_menu': create_menu(None),
                                                             'muc_tuyen_dung': muc_tuyen_dung,
                                                             'tuyendungs': tuyendungs,
                                                             'xu_ly_phan_trang':phan_trang(tuyendungs.number, tuyendungs.paginator.num_pages, 2),})

def tuyen_dung_chi_tiet(request, tuyen_dung_id):
    muc_tuyen_dung = Menu.objects.filter(menu_parent = Menu.objects.get(menu_link = '/tuyendung/'))
    tuyendung = get_object_or_404(TuyenDung, pk = tuyen_dung_id)
    cac_thong_tin_tuyen_dung_lien_quan = TuyenDung.objects.filter(menu=tuyendung.menu).exclude(pk=tuyendung.pk).order_by('-ngay_tao')[:8]
    

    return render(request, 'tuyendung/tuyendung_chi_tiet.html', {'main_menu': create_menu(None),
                                                             'muc_tuyen_dung': muc_tuyen_dung,
                                                             'tuyendung': tuyendung,
                                                             'cac_thong_tin_tuyen_dung_lien_quan': cac_thong_tin_tuyen_dung_lien_quan})

def in_tuyen_dung(request, tuyen_dung_id):
    tuyendung = get_object_or_404(TuyenDung, pk=tuyen_dung_id)
    return render(request, 'tuyendung/tuyendung_print.html', {'tuyendung': tuyendung})