from django.urls import path
from . import views

urlpatterns = [
    path('', views.dich_vu, name = 'dich_vu'),
    path('loaidichvu/<int:loai_dich_vu_id>', views.dich_vu_theo_loai, name = 'dich_vu_theo_loai'),
    path('chitiet/<int:dich_vu_id>', views.chi_tiet_dich_vu, name = 'chi_tiet_dich_vu'),
    path('print/chitiet/<int:dich_vu_id>', views.in_dich_vu, name='in_dich_vu' ),
    path('phidichvu/', views.phi_dich_vu, name='phi_dich_vu'),
    path('phidichvu/chitiet/<int:loai_phi_dich_vu_id>', views.phi_dich_vu_chi_tiet, name='phi_dich_vu_chi_tiet'),
    path('print/phidichvu/chitiet/<int:phi_dich_vu_id>', views.in_phi_dich_vu, name='in_phi_dich_vu'),
    path('khachhang/', views.khach_hang, name='khach_hang'),
    path('khachhang/danhmuc/<int:danh_muc_khach_hang_id>', views.khach_hang_theo_danh_muc, name='khach_hang_theo_danh_muc'),
]