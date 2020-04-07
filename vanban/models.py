from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.
class LoaiVanBan(models.Model):
    ten_loai_van_ban = models.CharField(max_length=255)
    thu_tu = models.IntegerField(default=0)

    def __str__(self):
        return self.ten_loai_van_ban

class VanBan(models.Model):
    loai_van_ban = models.ForeignKey(LoaiVanBan, on_delete=models.CASCADE)
    tieu_de = models.CharField(max_length=255)
    # loai_file = models.CharField(max_length=10)
    # kich_thuoc = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    so_lan_download = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    diem = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    xem = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    ngay_dang = models.DateTimeField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    file_upload = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.tieu_de

    def luot_xem(self):
        self.xem += 1
        self.save()

    def download(self):
        self.so_lan_download += 1
        self.save()

    def ngay_dang_ngan(self):
        local_now = timezone.localtime(self.ngay_dang)
        return local_now.strftime("%d/%m/%Y")