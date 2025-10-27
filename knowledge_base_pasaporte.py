#########################################################
## Base del conocimiento para el sistema de pasaportes. #
#########################################################

hechos = [

    # Costo de los pasaportes
    ('costo', '1_year', 885),
    ('costo', '3_year', 1730),
    ('costo', '6_year', 2350),
    ('costo', '10_year', 4120),

    # Restricciones para algunas vigencias
    ('vigencia_1_year_solo_menores_3', True),
    ('no_vigencia_10_year_agricolas', True),

    # Métodos de pago
    ('pago_en_oficinas_consulares', True),
    ('pago_en_bancos_autorizados', True),
    ('tramite_presencial', True),

    # Lista de los bancos autorizados
    ('banco_autorizado', 'banjercito'),
    ('banco_autorizado', 'banorte'),
    ('banco_autorizado', 'bbva'),
    ('banco_autorizado', 'banamex'),
    ('banco_autorizado', 'banbajio'),
    ('banco_autorizado', 'hsbc'),
    ('banco_autorizado', 'santander'),
    ('banco_autorizado', 'scotiabank'),

    # Hechos más generales de los tramites
    ('solo_titular_puede_tramitar', True),
    ('menores_requieren_tutor', True)
]

reglas = [

    # Descuento del 50%
    (('aplica_descuento_50', '?solicitante'),
     [('mayor_60', '?solicitante')]),

    (('aplica_descuento_50', '?solicitante'),
     [('tiene_discapacidad', '?solicitante')]),

    (('aplica_descuento_50', '?solicitante'),
     [('es_trabajador_agricola', '?solicitante')]),

    # Trabajadores agrícolas no pueden obtener vigencia de 10 años
    (('puede_vigencia', '?solicitante', '10_year'),
     [('es_trabajador_agricola', '?solicitante'), ('not', 'no_vigencia_10_year_agricolas')]),


    #Trámite por primera vez
    (('requisitos_primera_vez_mayor_edad', '?solicitante', '?requisitos'), 
     [('es_primera_vez', '?solicitante'), ('es_mayor_edad', '?solicitante'), 
      ('requiere_acreditar_nacionalidad', '?solicitante'), 
      ('requiere_identificacion_oficial', '?solicitante')]),

    # Pasaporte extraviado
    (('es_primera_vez', '?solicitante'), 
     [('pasaporte_extraviado', '?solicitante')]),
    
    (('es_primera_vez', '?solicitante'), 
     [('pasaporte_destruido', '?solicitante')]),
    
    (('es_primera_vez', '?solicitante'), 
     [('pasaporte_robado', '?solicitante')]),

    # Verificar el pago
    (('puede_realizar_tramite', '?solicitante'), 
     [('realizo_pago', '?solicitante')]),

    # Para los menores de edad
    (('requisitos_menor_edad', '?solicitante', '?requisitos'), 
     [('es_menor_edad', '?solicitante'), 
      ('requiere_autorizacion_tutores', '?solicitante'), 
      ('requiere_identificacion_tutores', '?solicitante')]),

    # Costo con el descuento aplicado
    (('costo_final', '?solicitante', '?vigencia', '?costo_final'), 
     [('costo', '?vigencia', '?costo_base'), 
      ('aplica_descuento_50', '?solicitante'), 
      ('divide', '?costo_base', 2, '?costo_final')]),
    
    (('costo_final', '?solicitante', '?vigencia', '?costo_base'), 
     [('costo', '?vigencia', '?costo_base'), 
      ('not', ('aplica_descuento_50', '?solicitante'))])
]

knowledge_base = []

for hecho in hechos:
    knowledge_base.append((hecho, []))

for regla in reglas:
    knowledge_base.append(regla)
