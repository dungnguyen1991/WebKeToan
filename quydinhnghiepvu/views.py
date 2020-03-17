from django.shortcuts import render, get_object_or_404
from trangchu.views import create_menu
from .models import QuyDinhNghiepVu
from trangchu.models import Menu
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from tintuc.views import phan_trang

# Create your views here.
def quy_dinh_nghiep_vu(request):
    danh_muc = Menu.objects.filter(menu_parent = Menu.objects.get(menu_link='/quydinhnghiepvu/'))
    list_danh_muc_nghiep_vu = QuyDinhNghiepVu.objects.filter(menu = danh_muc[0])
    
    # get trang hien tai
    page = request.GET.get('page', 1)

    # so trang
    paginator = Paginator(list_danh_muc_nghiep_vu, 2)
    
    try:
        danhmucnghiepvus = paginator.page(page)
    except PageNotAnInteger:
        danhmucnghiepvus = paginator.page(1)
    except EmptyPage:
        danhmucnghiepvus = paginator.page(paginator.num_pages)


    return render(request, 'quydinhnghiepvu/quydinhnghiepvu_main.html', {'main_menu':create_menu(None),
                                                                         'danh_muc': danh_muc,
                                                                         'danhmucnghiepvus': danhmucnghiepvus,
                                                                         'xu_ly_phan_trang':phan_trang(danhmucnghiepvus.number, danhmucnghiepvus.paginator.num_pages, 2)})

def quy_dinh_nghiep_vu_theo_danh_muc(request, danh_muc_id):
    danh_muc = Menu.objects.filter(menu_parent = Menu.objects.get(menu_link='/quydinhnghiepvu/'))
    list_danh_muc_nghiep_vu = QuyDinhNghiepVu.objects.filter(menu = get_object_or_404(Menu, pk=danh_muc_id))
    
    # get trang hien tai
    page = request.GET.get('page', 1)

    # so trang
    paginator = Paginator(list_danh_muc_nghiep_vu, 2)
    
    try:
        danhmucnghiepvus = paginator.page(page)
    except PageNotAnInteger:
        danhmucnghiepvus = paginator.page(1)
    except EmptyPage:
        danhmucnghiepvus = paginator.page(paginator.num_pages)

    return render(request, 'quydinhnghiepvu/quydinhnghiepvu_main.html', {'main_menu':create_menu(None),
                                                                         'danh_muc': danh_muc,
                                                                         'danhmucnghiepvus': danhmucnghiepvus,
                                                                         'xu_ly_phan_trang':phan_trang(danhmucnghiepvus.number, danhmucnghiepvus.paginator.num_pages, 2)})

def quy_dinh_nghiep_vu_chi_tiet(request, quy_dinh_nghiep_vu_id):
    danh_muc = Menu.objects.filter(menu_parent = Menu.objects.get(menu_link='/quydinhnghiepvu/'))
    quydinhnghiepvu = get_object_or_404(QuyDinhNghiepVu, pk=quy_dinh_nghiep_vu_id)
    quydinhnghiepvu_lien_quan = QuyDinhNghiepVu.objects.filter(menu = quydinhnghiepvu.menu).exclude(pk=quydinhnghiepvu.pk).order_by('-pk')[:8]
    return render(request, 'quydinhnghiepvu/quydinhnghiepvu_chi_tiet.html', {'main_menu':create_menu(None),
                                                                             'danh_muc': danh_muc,
                                                                             'quydinhnghiepvu':quydinhnghiepvu,
                                                                             'quydinhnghiepvu_lien_quan':quydinhnghiepvu_lien_quan,})


def in_quy_dinh_nghiep_vu(request, quy_dinh_nghiep_vu_id):
    quydinhnghiepvu = get_object_or_404(QuyDinhNghiepVu, pk=quy_dinh_nghiep_vu_id)
    return render(request, 'quydinhnghiepvu/quydinhnghiepvu_print.html', {'quydinhnghiepvu':quydinhnghiepvu})