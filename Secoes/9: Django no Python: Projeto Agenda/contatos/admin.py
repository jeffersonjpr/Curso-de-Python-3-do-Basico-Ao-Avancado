from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone',
                    'email', 'data_criacao', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome')
    list_filter = ('categoria', )
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone', 'email')
    list_editable = ('mostrar', 'telefone')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
