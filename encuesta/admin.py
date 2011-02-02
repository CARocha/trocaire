# -*- coding: UTF-8 -*-

from django.contrib import admin
from django.contrib.contenttypes import generic
from django.forms import CheckboxSelectMultiple
from models import *
from trocaire.lugar.models import *

class ComposicionHogarInline(generic.GenericStackedInline):
    model = ComposicionHogar
    max_num = 1
    fieldsets = [
        (None, {'fields': [('tiene_pareja', 'vive_con')]}),
        ('Habitantes del hogar', {'fields': ['cuantos_viven', ('entre0y6', 'entre7y17', 'entre18ymas')]}),
        ('Hijos', {'fields': [('tiene_hijos', 'cuantos_hijos'), ('hijos0y6', 'hijos7y17', 'hijos18ymas')]})
    ]

class InfoSocioEconomicaInline(generic.GenericStackedInline):    
    filter_horizontal = ['donde_trabaja', 'aportan']
    model = InformacionSocioEconomica
    max_num = 1

class AccesoControlRecursoInline(generic.GenericTabularInline):    
    model = AccesoControlRecurso    
    max_num = 1

class ConceptoViolenciaInline(generic.GenericTabularInline):
    model = ConceptoViolencia
    extra = 1

class ExpresionVBGInline(generic.GenericTabularInline):
    model = ExpresionVBG
    extra = 1

class CreenciaInline(generic.GenericTabularInline):
    model = Creencia
    extra = 1

class JustificacionVBGInline(generic.GenericTabularInline):
    model = JustificacionVBG
    extra = 1

class CausaVBGInline(generic.GenericTabularInline):
    model = CausaVBG
    extra = 1

class SituacionVBGInline(generic.GenericTabularInline):
    model = SituacionVBG
    max_num = 1

class AccionVBGInline(generic.GenericStackedInline):
    model = AccionVBG
    pregunta = '¿Qié hace Ud cuando existe una situación de VBG en su comunidad?'
    fieldsets = [
        (None, {'fields': ['ha_ayudado']}),
        (pregunta, {'fields': ['se_acerca', 'invita_actividad', 'no_hace_nada', 'no_hace_problema', 'busca_alternativa', 'no_sabe']}),
        (None, {'fields': ['donde_buscar', 'accion_tomar']})
    ]
    radio_fields = {
        'se_acerca': admin.HORIZONTAL,
        'invita_actividad': admin.HORIZONTAL,
        'no_hace_nada': admin.HORIZONTAL,
        'no_hace_problema': admin.HORIZONTAL,
        'busca_alternativa': admin.HORIZONTAL,
        'no_sabe': admin.HORIZONTAL
    }
    filter_horizontal = ['donde_buscar', 'accion_tomar']
    max_num = 1

class PrevalenciaVBGInline(generic.GenericStackedInline):
    verbose_name_plural = 'Prevalencia de la Violencia Basada en Género'
    verbose_name = 'Prevalencia de la VBG'
    model = PrevalenciaVBG
    filter_horizontal = ['quien',]
    max_num = 1

class AsuntoPublicoVBGInline(generic.GenericStackedInline):
    model = AsuntoPublicoVBG
    filter_horizontal = ['resolverse_con',]
    max_num = 1

class EfectoVBGInline(generic.GenericStackedInline):
    model = EfectoVBG
    filter_horizontal = ['como_afecta',]
    max_num = 1

class ConocimientoLeyInline(generic.GenericStackedInline):
    model = ConocimientoLey
    pregunta = 'Sabe Ud cuales de las siguientes acciones son prohibidas por la ley'
    fieldsets = [
        (None, {'fields': ['existe_ley', 'mencione']}),
        (pregunta, {'fields': [('padre_golpea', 'maestro_castiga', 'maestro_relacion'), ('joven_case', 'joven_relacion', 'patron_acoso'), ('lider_religioso', 'adulto_relacion', 'adulto_dinero')]}),
    ]
    max_num = 1

class TomaDecisionInline(generic.GenericStackedInline):
    model = TomaDecision
    filter_horizontal = ['decision',]
    max_num = 1

class ParticipacionPublicaInline(generic.GenericStackedInline):
    model = ParticipacionPublica
    filter_horizontal = ['espacio', 'motivo']
    max_num = 1

class IncidenciaPoliticaInline(generic.GenericTabularInline):
    model = IncidenciaPolitica
    max_num = 1

class CalidadAtencionInline(generic.GenericStackedInline):
    model = CalidadAtencion
    max_num = 1

class CorresponsabilidadInline(generic.GenericStackedInline):
    model = Corresponsabilidad
    max_num = 1
    pregunta = '¿Cuáles de las siguientes actividades realiza Ud en su hogar?'
    fieldsets = [
        (pregunta, {'fields': ['lavar', 'plancar', 'limpiar',
                                'jalar_agua', 'cuidar_ninos', 'hacer_mandados',
                                'llevar_lena', 'lavar_trastes', 'arreglar_cama',
                                'ir_reuniones', 'acompanar', 'hacer_compras',
                                'pagar_servicios', 'llevar_enfermos', 'cuidar_enfermos']}),
    ]
    radio_fields = {
        'lavar': admin.HORIZONTAL,
        'plancar': admin.HORIZONTAL,
        'limpiar': admin.HORIZONTAL,
        'jalar_agua': admin.HORIZONTAL,
        'cuidar_ninos': admin.HORIZONTAL,
        'hacer_mandados': admin.HORIZONTAL,
        'llevar_lena': admin.HORIZONTAL,
        'lavar_trastes': admin.HORIZONTAL,
        'arreglar_cama': admin.HORIZONTAL,
        'ir_reuniones': admin.HORIZONTAL,
        'acompanar': admin.HORIZONTAL,
        'hacer_compras': admin.HORIZONTAL,
        'pagar_servicios': admin.HORIZONTAL,
        'llevar_enfermos': admin.HORIZONTAL,
        'cuidar_enfermos': admin.HORIZONTAL,
    }

class ComunicacionAsertivaInline(generic.GenericStackedInline):
    model = ComunicacionAsertiva
    filter_horizontal = ['identifico', 'negociacion_exitosa']
    max_num = 1

class MujeresAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/files/css/especial.css", )
        }

        """js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')"""

    save_on_top = True
    actions_on_top = True
    inlines = [ComposicionHogarInline,
        InfoSocioEconomicaInline,
        AccesoControlRecursoInline,
        ConceptoViolenciaInline,
        ExpresionVBGInline,
        CreenciaInline,
        JustificacionVBGInline,
        CausaVBGInline,
        SituacionVBGInline,
        AccionVBGInline,
        PrevalenciaVBGInline,
        AsuntoPublicoVBGInline,
        EfectoVBGInline,
        ConocimientoLeyInline,
        TomaDecisionInline,
        ParticipacionPublicaInline,
        IncidenciaPoliticaInline,
        CalidadAtencionInline,
        CorresponsabilidadInline,
        ComunicacionAsertivaInline,
        ]

admin.site.register(Mujer, MujeresAdmin)
admin.site.register(ViveCon)
admin.site.register(LugarDeTrabajo)
admin.site.register(Recurso)
admin.site.register(Comunidad)
admin.site.register(Encuestador)
admin.site.register(Contraparte)
admin.site.register(Quien)
admin.site.register(ResolverVBG)
admin.site.register(ComoAfecta)
admin.site.register(TomaDecision)
admin.site.register(Espacio)
admin.site.register(MotivoParticipacion)
admin.site.register(SolucionConflicto)
admin.site.register(NegociacionExitosa)

class PrevalenciaVBGHombreInline(generic.GenericStackedInline):
    verbose_name_plural = 'Prevalencia de la Violencia Basada en Género'
    verbose_name = 'Prevalencia de la VBG'
    model = PrevalenciaVBGHombre
    filter_horizontal = ['quien',]
    max_num = 1

class HombresAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/files/css/especial.css", )
        }

        """js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')"""

    save_on_top = True
    actions_on_top = True
    inlines = [ComposicionHogarInline,
        InfoSocioEconomicaInline,
        AccesoControlRecursoInline,
        ConceptoViolenciaInline,
        ExpresionVBGInline,
        CreenciaInline,
        JustificacionVBGInline,
        CausaVBGInline,
        SituacionVBGInline,
        AccionVBGInline,
        PrevalenciaVBGHombreInline,
        AsuntoPublicoVBGInline,
        EfectoVBGInline,
        ConocimientoLeyInline,
        TomaDecisionInline,
        ParticipacionPublicaInline,
        IncidenciaPoliticaInline,
        CalidadAtencionInline,
        CorresponsabilidadInline,
        ComunicacionAsertivaInline,
        ]

admin.site.register(Hombre, HombresAdmin)

class InformacionSocioEconomicaLiderInline(generic.GenericStackedInline):
    filter_horizontal = ['donde_trabaja']
    model = InformacionSocioEconomicaLider
    max_num = 1

class AccionVBGLiderInline(generic.GenericStackedInline):
    model = AccionVBGLider
    pregunta = '¿Qié hace Ud cuando existe una situación de VBG en su comunidad?'
    fieldsets = [
        (None, {'fields': ['ha_ayudado']}),
        (pregunta, {'fields': ['se_acerca', 'invita_actividad', 'no_hace_nada', 'no_hace_problema', 'busca_alternativa', 'no_sabe']}),
        (None, {'fields': ['donde_buscar', 'accion_tomar']}),
        ('En su organización', {'fields': ['ud_previene', 'accion_prevenir', 'porque_no']})
    ]
    radio_fields = {
        'se_acerca': admin.HORIZONTAL,
        'invita_actividad': admin.HORIZONTAL,
        'no_hace_nada': admin.HORIZONTAL,
        'no_hace_problema': admin.HORIZONTAL,
        'busca_alternativa': admin.HORIZONTAL,
        'no_sabe': admin.HORIZONTAL
    }
    filter_horizontal = ['donde_buscar', 'accion_tomar', 'accion_prevenir']
    max_num = 1

class PrevalenciaVBGLiderInline(generic.GenericStackedInline):
    verbose_name_plural = 'Prevalencia de la Violencia Basada en Género'
    verbose_name = 'Prevalencia de la VBG'
    model = PrevalenciaVBGLider
    filter_horizontal = ['quien',]
    max_num = 1

class LiderAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("/files/css/especial.css", )
        }

        """js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')"""

    save_on_top = True
    actions_on_top = True
    inlines = [InformacionSocioEconomicaLiderInline,        
        ConceptoViolenciaInline,
        ExpresionVBGInline,
        CreenciaInline,
        JustificacionVBGInline,
        CausaVBGInline,
        SituacionVBGInline,
        AccionVBGLiderInline,
        PrevalenciaVBGLiderInline,
        AsuntoPublicoVBGInline,
        EfectoVBGInline,
        ConocimientoLeyInline,
        TomaDecisionInline,        
        IncidenciaPoliticaInline,
        CalidadAtencionInline,
        CorresponsabilidadInline,
        ComunicacionAsertivaInline,
        ]

admin.site.register(Lider, LiderAdmin)