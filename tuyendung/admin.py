from django.contrib import admin
from .models import TuyenDung
from trangchu.models import Menu


# Register your models here.
class TuyenDungAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "menu":
            kwargs["queryset"] = Menu.objects.filter(menu_parent=Menu.objects.get(menu_link='/tuyendung/'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(TuyenDung, TuyenDungAdmin)