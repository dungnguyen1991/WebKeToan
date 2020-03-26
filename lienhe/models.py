from django.db import models

# Create your models here.
class FeedBack(models.Model):
    hoten = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    tencongty = models.CharField(max_length=255)
    diachi = models.CharField(max_length=255)
    dienthoai = models.CharField(max_length=10)
    fax = models.CharField(max_length=10)
    guiden = models.EmailField(max_length=255)
    tieude = models.CharField(max_length=255)
    noidung = models.TextField()

    def __str__(self):
        return self.tieude