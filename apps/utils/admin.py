from django.contrib import admin

from . models import Regiao, Estado, Cidade

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 0


class EstadoInline(admin.TabularInline):
    model = Estado
    extra = 0


class EstadoAdmin(admin.ModelAdmin):
    list_display = ['nome','regiao']
    list_filter = ['regiao']
    search_fields = ['nome', 'regiao__nome']
    inlines = [
    CidadeInline,

    ]

class RegiaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sigla']
    list_filter = ['nome']
    search_fields = ['nome']
    inlines = [
    EstadoInline,
    ]

admin.site.register(Regiao, RegiaoAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Cidade)
