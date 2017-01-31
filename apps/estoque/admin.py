from django.contrib import admin

from . models import Produto, Fabricante, Marca, Categoria



#INLINES

class MarcaInline(admin.TabularInline):
    model = Marca
    extra = 0

class ProdutoInline(admin.TabularInline):
    model = Produto
    extra = 0

#MODEL ADMIN


class FabricanteAdmin(admin.ModelAdmin):

    list_display = ['nome','endereco','cnpj','cidade']
    list_filter = ['nome']
    search_fields = ['nome']

    inlines = [
        MarcaInline,
    ]

class MarcaAdmin(admin.ModelAdmin):

    list_display = ['nome', 'fabricante']
    list_filter = ['nome']
    search_fields = ['nome', 'fabricante__nome']
    inlines = [
        ProdutoInline,

    ]

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nome','marca']
    list_filter = ['marca']
    search_fields = ['marca__nome']


admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Marca, MarcaAdmin)
