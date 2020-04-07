from django.urls import path
from . import views

urlpatterns = [
    path('', views.vanban, name='ban_ban'),
    path('loaivanban/<int:loai_van_ban_id>', views.hien_thi_van_ban_theo_loai, name='hien_thi_van_ban_theo_loai'),
    path('chitiet/<int:van_ban_id>', views.van_ban_chi_tiet, name = 'van_ban_chi_tiet'),
    path('download/<int:van_ban_id>', views.van_ban_download, name = 'van_ban_download'),
]