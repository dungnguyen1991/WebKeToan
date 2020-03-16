from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.exceptions import MultipleObjectsReturned
from trangchu.views import create_menu
from trangchu.models import Menu
from .models import DichVu,PhiDichVu
from tintuc.views import phan_trang
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def dich_vu(request):
    danh_muc_dich_vu = Menu.objects.filter(menu_parent = Menu.objects.get(menu_link='/dichvu/'))
    cac_dich_vu = DichVu.objects.filter(menu = danh_muc_dich_vu[0]).order_by('pk')

    # get trang hien tai
    page = request.GET.get('page', 1)

    # so item tren 1 trang
    paginator = Paginator(cac_dich_vu, 4)
    
    try:
        dichvus = paginator.page(page)
    except PageNotAnInteger:
        dichvus = paginator.page(1)
    except EmptyPage:
        dichvus = paginator.page(paginator.num_pages)

    return render(request,'dichvu/dichvu_main.html', {'danh_muc_dich_vu': danh_muc_dich_vu,
                                                        'dichvus': dichvus,
                                                        'xu_ly_phan_trang':phan_trang(dichvus.number, dichvus.paginator.num_pages, 2),
                                                        'main_menu': create_menu(None)})

def dich_vu_theo_loai(request, loai_dich_vu_id):
    danh_muc_dich_vu = Menu.objects.filter(menu_parent = Menu.objects.get(menu_link='/dichvu/'))
    cac_dich_vu = DichVu.objects.filter(menu = get_object_or_404(Menu, pk=loai_dich_vu_id)).order_by('pk')

    # get trang hien tai
    page = request.GET.get('page', 1)

    # so item tren 1 trang
    paginator = Paginator(cac_dich_vu, 4)
    
    try:
        dichvus = paginator.page(page)
    except PageNotAnInteger:
        dichvus = paginator.page(1)
    except EmptyPage:
        dichvus = paginator.page(paginator.num_pages)

    return render(request, 'dichvu/dichvu_main.html', {'danh_muc_dich_vu': danh_muc_dich_vu,
                                                        'dichvus': dichvus,
                                                        'xu_ly_phan_trang':phan_trang(dichvus.number, dichvus.paginator.num_pages, 2),
                                                        'main_menu': create_menu(None),
                                                        })

def chi_tiet_dich_vu(request, dich_vu_id):
    danh_muc_dich_vu = Menu.objects.filter(menu_parent = Menu.objects.get(menu_link='/dichvu/'))
    dichvu = get_object_or_404(DichVu, pk=dich_vu_id)
    cac_dich_vu_lien_quan = DichVu.objects.filter(menu=dichvu.menu).exclude(pk=dichvu.pk)[:8]
    return render(request,'dichvu/dichvu_chi_tiet.html', {'danh_muc_dich_vu':danh_muc_dich_vu,
                                                            'dichvu':dichvu,
                                                            'main_menu': create_menu(None),
                                                            'cac_dich_vu_lien_quan':cac_dich_vu_lien_quan,})

def in_dich_vu(request, dich_vu_id):
    dichvu = get_object_or_404(DichVu, pk=dich_vu_id)
    return render(request, 'dichvu/dichvu_print.html', {'dichvu':dichvu})


# Thanh phan phi dich vu
def phi_dich_vu(request):
    danh_muc_phi_dich_vu = Menu.objects.filter(menu_parent = Menu.objects.get(menu_link='/dichvu/phidichvu/'))
    
    try:
        phidichvu = get_object_or_404(PhiDichVu, menu=danh_muc_phi_dich_vu[0])
    except MultipleObjectsReturned:
        phidichvu = get_list_or_404(PhiDichVu, menu=danh_muc_phi_dich_vu[0])[0]

    return render(request,'dichvu/phidichvu_chi_tiet.html', {'danh_muc_phi_dich_vu':danh_muc_phi_dich_vu,
                                                          'phidichvu':phidichvu,
                                                          'main_menu': create_menu(None),})

def phi_dich_vu_chi_tiet(request, loai_phi_dich_vu_id):
    danh_muc_phi_dich_vu = Menu.objects.filter(menu_parent = Menu.objects.get(menu_link='/dichvu/phidichvu/'))
    
    try:
        phidichvu = get_object_or_404(PhiDichVu, menu =  get_object_or_404(Menu, pk=loai_phi_dich_vu_id))
    except MultipleObjectsReturned:
        phidichvu = get_list_or_404(PhiDichVu, menu=get_object_or_404(Menu, pk=loai_phi_dich_vu_id))[0]
    
    return render(request,'dichvu/phidichvu_chi_tiet.html', {'danh_muc_phi_dich_vu':danh_muc_phi_dich_vu,
                                                          'phidichvu':phidichvu,
                                                          'main_menu': create_menu(None),})

def in_phi_dich_vu(request, phi_dich_vu_id):
    phidichvu = get_object_or_404(PhiDichVu, pk=phi_dich_vu_id)
    return render(request, 'dichvu/phidichvu_print.html', {'phidichvu':phidichvu})