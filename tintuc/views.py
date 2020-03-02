from django.shortcuts import render
from .models import LoaiTinTuc, TinTuc
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
def index(request):
    return render(request, 'tintuc/index.html')

def tat_ca_tin_tuc(request):
    loaitintucs = LoaiTinTuc.objects.all()
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

    return render(request, 'tintuc/tintuc_main.html', {'loaitintucs':loaitintucs, 'tintucs':tintucs,
                                                       'xu_ly_phan_trang':phan_trang(tintucs.number, tintucs.paginator.num_pages, 2)})

def tin_tuc_theo_loai(request, loai_tin_tuc_id):
    loaitintucs = LoaiTinTuc.objects.all()
    loai_tin_tuc_duoc_chon = LoaiTinTuc.objects.get(pk=loai_tin_tuc_id)
    danh_sach_tintucs = TinTuc.objects.filter(loai_tin_tuc=loai_tin_tuc_duoc_chon).order_by('-ngay_tao')

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
                                                        'xu_ly_phan_trang':phan_trang(tintucs.number, tintucs.paginator.num_pages, 2)})

def tin_tuc_chi_tiet(request, tin_tuc_id):
    loaitintucs = LoaiTinTuc.objects
    tintuc = TinTuc.objects.get(pk=tin_tuc_id)
    cac_tin_tuc_lien_quan = TinTuc.objects.filter(loai_tin_tuc=tintuc.loai_tin_tuc).exclude(pk=tintuc.pk).order_by('-ngay_tao')[:8]
    return render(request, 'tintuc/tintuc_chi_tiet.html', {'loaitintucs':loaitintucs,
                                                        'tintuc':tintuc,
                                                        'cac_tin_tuc_lien_quan':cac_tin_tuc_lien_quan})

def in_tin_tuc(request, tin_tuc_id):
    tintuc = TinTuc.objects.get(pk=tin_tuc_id)
    return render(request, 'tintuc/tintuc_print.html', {'tintuc':tintuc})