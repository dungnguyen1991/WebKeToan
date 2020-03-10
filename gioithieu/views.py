from django.shortcuts import render

# Create your views here.
def gioi_thieu_cong_ty(request):
    return render(request, 'gioithieu/gioithieu_chitiet.html')