from django.contrib import admin
from . import models

@admin.register(models.blog_crud)
class BlogCRUDAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'creditos')
    search_fields = ('codigo', 'nombre')
    list_filter = ('creditos',)