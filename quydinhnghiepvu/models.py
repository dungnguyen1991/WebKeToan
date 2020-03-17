from django.db import models
from trangchu.models import Menu
# Create your models here.
class QuyDinhNghiepVu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, default = 1)
    tieu_de = models.CharField(max_length = 255)
    mo_ta_ngan = models.TextField()
    image = models.ImageField(upload_to='images/')
    noi_dung = models.TextField()

    def __str__(self):
        return self.tieu_de