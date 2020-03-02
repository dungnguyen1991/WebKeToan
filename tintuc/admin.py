from django.contrib import admin
from .models import TinTuc, LoaiTinTuc

# class TinTucAdmin(admin.ModelAdmin):
#     list_display = ('title','lead','date')
#     class Media:
#         js = ('/media/js/nicEdit.js', '/media/js/textarea_content.js')

# Register your models here.
admin.site.register(TinTuc)
admin.site.register(LoaiTinTuc)