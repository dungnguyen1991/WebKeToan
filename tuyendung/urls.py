from django.urls import path
from . import views

urlpatterns = [
    path('', views.tuyen_dung, name='tuyen_dung'),
    path('danhmuc/<int:danh_muc_id>', views.danh_muc_tuyen_dung, name='danh_muc_tuyen_dung'),
    path('chitiet/<int:tuyen_dung_id>', views.tuyen_dung_chi_tiet, name='tuyen_dung_chi_tiet'),
    path('print/chitiet/<int:tuyen_dung_id>', views.in_tuyen_dung, name='in_tuyen_dung' ),
]