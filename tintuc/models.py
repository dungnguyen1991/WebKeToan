from django.db import models
import pytz
from django.utils import timezone
from trangchu.models import Menu

# Create your models here.
class LoaiTinTuc(models.Model):
    ten_loai_tin_tuc = models.CharField(max_length = 255)

    def __str__(self):
        return self.ten_loai_tin_tuc



class TinTuc(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, default = 1)
    tieu_de = models.CharField(max_length = 255)
    ngay_tao = models.DateTimeField()
    mo_ta_ngan = models.TextField()
    image = models.ImageField(upload_to='images/')
    noi_dung = models.TextField()

    def __str__(self):
        return self.tieu_de

    def ngay_tao_ngan(self):
        local_now = timezone.localtime(self.ngay_tao)
        return local_now.strftime("%d/%m/%Y")

    def ngay_tao_danh_muc(self):
        local_now = timezone.localtime(self.ngay_tao)
        return local_now.strftime("%d/%m/%Y, %H:%M")       

    def ngay_tao_day_du(self):
        # ngay_tao_dai =  type(self.ngay_tao.strftime("%w"))

        # vn = timezone('Asia/Ho_Chi_Minh')

        # loc_dt = vn.localize(self.ngay_tao)

        local_now = timezone.localtime(self.ngay_tao)

        switcher = {
            0:"Chủ nhật",
            1:"Thứ hai",
            2:"Thứ ba",
            3:"Thứ tư",
            4:"Thứ năm",
            5:"Thứ sáu",
            6:"Thứ bảy"
        }

        ngay_tao_dai = switcher.get(int(local_now.strftime("%w")))

        ngay_tao_dai = ngay_tao_dai + ", " + local_now.strftime("%d/%m/%Y, %H:%M UTC%Z")

        return ngay_tao_dai