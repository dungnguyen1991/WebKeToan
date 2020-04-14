from django.db import models

# Create your models here.
class CauHoi(models.Model):
    ho_ten = models.CharField(max_length=255)
    email = models.EmailField()
    danh_muc = models.PositiveSmallIntegerField()
    noi_dung = models.TextField()

    def __str__(self):
        return self.noi_dung

class TraLoi(models.Model):
    cau_hoi = models.OneToOneField(CauHoi,
                                   on_delete = models.CASCADE,
                                   primary_key = True)
    dap_an = models.TextField()

    def __str__(self):
        return self.cau_hoi.noi_dung