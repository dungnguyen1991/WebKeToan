from django.db import models
from trangchu.models import Menu

# Create your models here.
class GioiThieu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    tieu_de = models.CharField(max_length=255)
    noi_dung = models.TextField()

    def __str__(self):
        return self.tieu_de