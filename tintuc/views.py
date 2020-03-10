from django.shortcuts import render
from .models import  TinTuc
from trangchu.models import Menu
from trangchu.views import create_menu
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def phan_trang(trang_hien_tai, tong_so_trang, so_trang_hien_thi):
     # phan trang
    xu_ly_phan_trang = {}
    # so_trang_hien_thi = 3
    # start = tintucs.number - so_trang_hien_thi
    # end = tintucs.number + so_trang_hien_thi

    start = trang_hien_tai - so_trang_hien_thi
    end = trang_hien_tai + so_trang_hien_thi
    xu_ly_phan_trang['chuyen_den_trang_dau'] = True
    xu_ly_phan_trang['chuyen_den_trang_cuoi'] = True

    if start <= 1:
        xu_ly_phan_trang['trang_bat_dau'] = 1
        xu_ly_phan_trang['chuyen_den_trang_dau'] = False
    elif start >= tong_so_trang - so_trang_hien_thi*2:
        xu_ly_phan_trang['trang_bat_dau'] = tong_so_trang - so_trang_hien_thi*2
    else:
        xu_ly_phan_trang['trang_bat_dau'] = start

    if end >= tong_so_trang:
        xu_ly_phan_trang['trang_ket_thuc'] = tong_so_trang
        xu_ly_phan_trang['chuyen_den_trang_cuoi'] = False
    elif end <= so_trang_hien_thi*2:
        xu_ly_phan_trang['trang_ket_thuc'] = so_trang_hien_thi*2
    else:
        xu_ly_phan_trang['trang_ket_thuc'] = end

    return xu_ly_phan_trang

    # ket thuc phan trang

# Create your views here.
# def index(request):
#     return render(request, 'tintuc/index.html')

def tat_ca_tin_tuc(request):
    loaitintucs = Menu.objects.filter(menu_parent=Menu.objects.get(menu_link='/tintuc/'))
    danh_sach_tintucs = TinTuc.objects.order_by('-ngay_tao')
    
    # get trang hien tai
    page = request.GET.get('page', 1)

    # so trang
    paginator = Paginator(danh_sach_tintucs, 2)
    
    try:
        tintucs = paginator.page(page)
    except PageNotAnInteger:
        tintucs = paginator.page(1)
    except EmptyPage:
        tintucs = paginator.page(paginator.num_pages)

    return render(request, 'tintuc/tintuc_main.html', {'loaitintucs':loaitintucs, 'tintucs':tintucs, "main_menu": create_menu(None),
                                                       'xu_ly_phan_trang':phan_trang(tintucs.number, tintucs.paginator.num_pages, 2)})

def tin_tuc_theo_loai(request, loai_tin_tuc_id):
    loaitintucs = Menu.objects.filter(menu_parent=Menu.objects.get(menu_link='/tintuc/'))
    loai_tin_tuc_duoc_chon = Menu.objects.get(pk=loai_tin_tuc_id)
    danh_sach_tintucs = TinTuc.objects.filter(menu=loai_tin_tuc_duoc_chon).order_by('-ngay_tao')

     # get trang hien tai
    page = request.GET.get('page', 1)

    # so trang
    paginator = Paginator(danh_sach_tintucs, 2)
    
    try:
        tintucs = paginator.page(page)
    except PageNotAnInteger:
        tintucs = paginator.page(1)
    except EmptyPage:
        tintucs = paginator.page(paginator.num_pages)
        
    return render(request, 'tintuc/tintuc_main.html', {'loaitintucs':loaitintucs,
                                                        'tintucs':tintucs,
                                                        'loai_tin_tuc_duoc_chon':loai_tin_tuc_duoc_chon,
                                                        "main_menu": create_menu(None),
                                                        'xu_ly_phan_trang':phan_trang(tintucs.number, tintucs.paginator.num_pages, 2)})

def tin_tuc_chi_tiet(request, tin_tuc_id):
    loaitintucs = Menu.objects.filter(menu_parent=Menu.objects.get(menu_link='/tintuc/'))
    tintuc = TinTuc.objects.get(pk=tin_tuc_id)
    cac_tin_tuc_lien_quan = TinTuc.objects.filter(menu=tintuc.menu).exclude(pk=tintuc.pk).order_by('-ngay_tao')[:8]
    return render(request, 'tintuc/tintuc_chi_tiet.html', {'loaitintucs':loaitintucs,
                                                        'tintuc':tintuc,
                                                        "main_menu": create_menu(None),
                                                        'cac_tin_tuc_lien_quan':cac_tin_tuc_lien_quan})

def in_tin_tuc(request, tin_tuc_id):
    tintuc = TinTuc.objects.get(pk=tin_tuc_id)
    return render(request, 'tintuc/tintuc_print.html', {'tintuc':tintuc})