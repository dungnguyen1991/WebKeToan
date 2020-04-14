from django.shortcuts import render
from trangchu.views import create_menu
from .models import FeedBack

# Create your views here.
def lien_he(request):
    if request.method == 'POST':
        for key in request.POST:
            if len(request.POST[key].strip()) == 0:
                action = 'Xin nhập tất cả nội dung có đánh dấu *'
                return render(request, 'lienhe/lienhe.html',{'main_menu': create_menu(None),'action': action})

        fb = FeedBack(hoten = request.POST['hoten'],
                      email = request.POST['email'],
                      tencongty = request.POST['tencongty'],
                      diachi = request.POST['diachi'],
                      dienthoai = request.POST['dienthoai'],
                      fax = request.POST['fax'],
                      guiden = request.POST['guiden'],
                      tieude = request.POST['tieude'],
                      noidung = request.POST['noidung'])
        fb.save()

        action = 'Xin cảm ơn phản hồi của bạn!'
        return render(request, 'lienhe/lienhe.html',{'main_menu': create_menu(None),'action': action})
    else:
        return render(request, 'lienhe/lienhe.html',{'main_menu': create_menu(None),})