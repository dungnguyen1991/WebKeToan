from django.urls import path
from . import views

urlpatterns = [
    path('', views.quy_dinh_nghiep_vu, name='quy_dinh_nghiep_vu'),
    path('danhmuc/<int:danh_muc_id>', views.quy_dinh_nghiep_vu_theo_danh_muc, name='quy_dinh_nghiep_vu_theo_danh_muc'),
    path('chitiet/<int:quy_dinh_nghiep_vu_id>', views.quy_dinh_nghiep_vu_chi_tiet, name='quy_dinh_nghiep_vu_chi_tiet'),
    path('print/chitiet/<int:quy_dinh_nghiep_vu_id>', views.in_quy_dinh_nghiep_vu, name='in_quy_dinh_nghiep_vu' ),
]