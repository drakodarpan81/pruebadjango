from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import CatArticulo, CatProveedor

# Register your models here.
admin.site.register(CatProveedor)

class ArticuloAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('descripcion_articulo',)

admin.site.register(CatArticulo, ArticuloAdmin)