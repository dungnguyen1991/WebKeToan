from django.contrib import admin
from .models import QuyDinhNghiepVu
from trangchu.models import Menu

# Register your models here.
class QuyDinhNghiepVuAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "menu":
            # Menu.objects.get(menu_title='dung')
            # kwargs["queryset"] = Car.objects.filter(owner=request.user)
            kwargs["queryset"] = Menu.objects.filter(menu_parent=Menu.objects.get(menu_link='/quydinhnghiepvu/'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(QuyDinhNghiepVu, QuyDinhNghiepVuAdmin)