from django.contrib import admin

from . models import Produto, Fabricante, Marca, Categoria, Estoque,Prateleira,Lote



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
    list_display = ['codigo','nome','marca', 'categoria']
    list_filter = ['marca', 'categoria' ]
    search_fields = ['marca__nome']


class PrateleiraAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'categoria']
    list_filter = ['categoria']
    search_fields = ['categoria']


class EstoqueAdmin(admin.ModelAdmin):
    list_display = ['lote']
    search_fields = ['lote']


class LoteAdmin(admin.ModelAdmin):
    list_display = ['codigo','produto','data_validade']
    search_fields = ['produto']


admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Prateleira, PrateleiraAdmin)
admin.site.register(Estoque, EstoqueAdmin)
admin.site.register(Lote, LoteAdmin)
