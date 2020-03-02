from django.db import models

# Create your models here.
class Menu(models.Model):
    menu_parent = models.ForeignKey('self', on_delete=models.CASCADE, default = None,  blank=True, null=True)
    menu_title = models.CharField(max_length = 255, unique=True)
    menu_link = models.CharField(max_length=500)

    def __str__(self):
        return self.menu_title