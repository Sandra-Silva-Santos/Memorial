from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Memorial



class MemorialResource(resources.ModelResource):
    class Meta:
        model = Memorial
        fields = ('id','num_obtuario', 'falecido', 'data_nascimento', 'sexo', 'idade', 'cor', 'data_falecimento', 'detalhes')
        export_order = ('id','num_obtuario', 'falecido', 'data_nascimento', 'sexo', 'idade', 'cor', 'data_falecimento', 'detalhes')
        


@admin.register(Memorial)
class MemorialAdmin(ImportExportModelAdmin):
    resource_class = MemorialResource
    list_display = ('num_obtuario', 'falecido', 'data_nascimento', 'sexo', 'idade', 'data_falecimento')
    search_fields = ['falecido', 'num_obtuario']
    list_filter = ['num_obtuario' , 'data_nascimento' ,'data_falecimento']
    
 

admin.site.site_header = 'Sistema de Gerenciamento Memorial'
admin.site.add_action('export_as_json', 'Exportar para JSON')
admin.site.add_action('export_as_csv', 'Exportar para CSV')
admin.site.add_action('export_as_xls', 'Exportar para XLS')

