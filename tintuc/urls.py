from django.urls import path
from . import views

urlpatterns = [
    path('', views.tat_ca_tin_tuc, name= 'tintuc'),
    path('loaitintuc/<int:loai_tin_tuc_id>', views.tin_tuc_theo_loai, name='tin_tuc_theo_loai'),
    path('chitiet/<int:tin_tuc_id>', views.tin_tuc_chi_tiet, name='tin_tuc_chi_tiet'),
    path('print/chitiet/<int:tin_tuc_id>', views.in_tin_tuc, name='in_tin_tuc' ),
]