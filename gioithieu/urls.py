from django.urls import path
from . import views

urlpatterns = [
    path('', views.gioi_thieu, name= 'gioi_thieu'),
    path('chitiet/<int:gioi_thieu_id>', views.chi_tiet, name= 'chi_tiet'),
]