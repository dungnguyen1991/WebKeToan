from django.shortcuts import render, get_object_or_404
from trangchu.views import create_menu
import os
from .models import LoaiVanBan, VanBan
import zipfile
from io import BytesIO

from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tintuc.views import phan_trang

# Create your views here.

def vanban(request):
    ds_loaivanban = LoaiVanBan.objects.all()
    ds_vanban = VanBan.objects.all().order_by('-pk')
    
    # get trang hien tai
    page = request.GET.get('page', 1)

    # so van ban trong mot trang
    paginator = Paginator(ds_vanban, 2)
    
    try:
        vanbans = paginator.page(page)
    except PageNotAnInteger:
        vanbans = paginator.page(1)
    except EmptyPage:
        vanbans = paginator.page(paginator.num_pages)

    return render(request, 'vanban/vanban_danhmuc.html', {'main_menu': create_menu(None),
                                                          'ds_loaivanban': ds_loaivanban,
                                                          'vanbans': vanbans,
                                                          'xu_ly_phan_trang':phan_trang(vanbans.number, vanbans.paginator.num_pages, 2),})

def hien_thi_van_ban_theo_loai(request, loai_van_ban_id):
    ds_loaivanban = LoaiVanBan.objects.all()
    loai_van_ban_duoc_chon = get_object_or_404(LoaiVanBan, pk=loai_van_ban_id)
    ds_vanban = VanBan.objects.filter(loai_van_ban=loai_van_ban_duoc_chon).order_by('-pk')
    
    # get trang hien tai
    page = request.GET.get('page', 1)

    # so van ban trong mot trang
    paginator = Paginator(ds_vanban, 2)
    
    try:
        vanbans = paginator.page(page)
    except PageNotAnInteger:
        vanbans = paginator.page(1)
    except EmptyPage:
        vanbans = paginator.page(paginator.num_pages)

    return render(request, 'vanban/vanban_danhmuc.html', {'main_menu': create_menu(None),
                                                          'ds_loaivanban': ds_loaivanban,
                                                          'loai_van_ban_duoc_chon': loai_van_ban_duoc_chon,
                                                          'vanbans': vanbans,
                                                          'xu_ly_phan_trang':phan_trang(vanbans.number, vanbans.paginator.num_pages, 2),})

def van_ban_chi_tiet(request, van_ban_id):
    ds_loaivanban = LoaiVanBan.objects.all()
    van_ban = get_object_or_404(VanBan, pk = van_ban_id)
    cac_van_ban_lien_quan = VanBan.objects.filter(loai_van_ban=van_ban.loai_van_ban).exclude(pk=van_ban.pk).order_by('-pk')[:8]
    van_ban.luot_xem()
    fp = van_ban.file_upload.url
    ext = os.path.splitext(fp)[-1].lower()
    filesize = os.path.getsize(fp[1:])
    return render(request, 'vanban/vanban_chitiet.html', {'main_menu': create_menu(None),
                                                          'ds_loaivanban': ds_loaivanban,
                                                          'van_ban': van_ban,
                                                          'cac_van_ban_lien_quan': cac_van_ban_lien_quan,
                                                          'ext': ext[1:],
                                                          'filesize': int(filesize/1024)})


def van_ban_download(request, van_ban_id):
    van_ban = get_object_or_404(VanBan, pk = van_ban_id)
    f = van_ban.file_upload.url[1:]

    byte_data = BytesIO()
    zip_file = zipfile.ZipFile(byte_data, "w")
    
    filename = os.path.basename(os.path.normpath(f))
    zip_file.write(f, filename)

    zip_file.close()

    response = HttpResponse(byte_data.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=van_ban.zip'

    van_ban.download()

    return response