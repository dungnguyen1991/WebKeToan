from django.urls import path
from . import views

urlpatterns = [
    path('', views.gioi_thieu_cong_ty, name= 'gioi_thieu_cong_ty'),
]