from django.contrib import admin
from .models import TinTuc
from trangchu.models import Menu

# class TinTucAdmin(admin.ModelAdmin):
#     list_display = ('title','lead','date')
#     class Media:
#         js = ('/media/js/nicEdit.js', '/media/js/textarea_content.js')

# Register your models here.

class TinTucAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "menu":
            # Menu.objects.get(menu_title='dung')
            # kwargs["queryset"] = Car.objects.filter(owner=request.user)
            kwargs["queryset"] = Menu.objects.filter(menu_parent=Menu.objects.get(menu_link='/tintuc/'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(TinTuc, TinTucAdmin)