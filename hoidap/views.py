from django.shortcuts import render, redirect, get_object_or_404
from trangchu.views import create_menu
from .models import TraLoi, CauHoi
# Create your views here.

def hoi_dap(request):
    tralois = TraLoi.objects.all().order_by('-pk')
    return render(request, 'hoidap/hoidap_main.html', {'main_menu': create_menu(None),
                                                       'tralois': tralois,})

def hoi_dap_chi_tiet(request, cau_hoi_id):
    tralois = TraLoi.objects.all().order_by('-pk')
    cau_hoi_duoc_chon = get_object_or_404(CauHoi, pk=cau_hoi_id)
    return render(request, 'hoidap/hoidap_main.html', {'main_menu': create_menu(None),
                                                       'tralois': tralois,
                                                       'cau_hoi_duoc_chon': cau_hoi_duoc_chon,})

def gui_cau_hoi(request):
        if request.method == "POST":
            for key in request.POST:
                if len(request.POST[key].strip()) == 0:
                    action = 'Xin nhập tất cả nội dung có đánh dấu *'
                    return render(request,
                                  'hoidap/hoidap_guicauhoi.html',
                                  {'main_menu': create_menu(None),
                                   'action': action})

            question = CauHoi(ho_ten = request.POST['hoten'],
                              email = request.POST['email'],
                              danh_muc = request.POST['danhmuc'],
                              noi_dung = request.POST['noidung'])
            question.save()
            return redirect('hoi_dap')
        else:
            return render(request, 'hoidap/hoidap_guicauhoi.html', {'main_menu': create_menu(None)})