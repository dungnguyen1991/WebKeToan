from django.urls import path
from . import views

urlpatterns = [
    path('', views.hoi_dap, name='hoi_dap'),
    path('chitiet/<int:cau_hoi_id>', views.hoi_dap_chi_tiet, name='hoi_dap_chi_tiet'),
    path('guicauhoi', views.gui_cau_hoi, name='gui_cau_hoi'),
]