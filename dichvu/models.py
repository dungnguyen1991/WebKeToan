from django.db import models
from trangchu.views import Menu

# Create your models here.
class DichVu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    tieu_de =  models.CharField(max_length=255)
    noi_dung = models.TextField()

    def __str__(self):
        return self.tieu_de

class PhiDichVu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    tieu_de =  models.CharField(max_length=255)
    noi_dung = models.TextField()

    def __str__(self):
        return self.tieu_de

class KhachHang(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    tieu_de =  models.CharField(max_length=255)
    noi_dung = models.TextField()

    def __str__(self):
        return self.tieu_de