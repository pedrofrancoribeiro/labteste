#coding: utf-8
#define as tabelas de objetos do sistema

#tabela baixa1
db.define_table('baixa1',
    Field('dia_hora','datetime',label='timestamp', unique=True),
    Field('record','integer',label='registro'),
    Field('batt_volt_min','double',label='batt_volt'),
    Field('p_temp','double',label='p_temp'),
    Field('nr_lite_avg','double',label='nr_lite'),
    Field('cm3_up_avg','double',label='cm3_up'),
    Field('cm3_dn_avg','double',label='cm3_dn'),
    Field('cg3_up_corr_avg','double',label='cg3_up'),
    Field('cg3_dn_corr_avg', 'double',label='cg3_dn'),
    Field('cnr1_tc_avg','double',label='cnr1_tc'),
    Field('cma11_up_avg','double',label='cma11_up'),
    Field('cma11_dn_avg','double',label='cma11_dn'),
    Field('li_190s_avg','double',label='li190s'),
    Field('vw_avg','double',label='vw'),
    Field('hfp01_avg','double',label='hfp01'),
    Field('stp01_50cm_avg','double',label='stp01_50cm'),
    Field('stp01_20cm_avg','double',label='stp01_20cm'),
    Field('stp01_10cm_avg','double',label='stp01_10cm'),
    Field('stp01_05cm_avg','double',label='stp01_05cm'),
    Field('stp01_02cm_avg','double',label='stp01_02cm'),
    Field('cs106_avg','double',label='cs106'),
    Field('hmp45c_temp_avg','double',label='hmp45c_temp'),
    Field('hmp45c_rh_avg','double',label='hmp45c_rh'),
    Field('wind_speed','double',label='wind_speed'),
    Field('win_direction','double',label='windirection'),
    Field('tb4_tot','double',label='tb4_tot')
)

#tabela baixa2
db.define_table('baixa2',
    Field('dia_hora','datetime',label='timestamp', unique=True),
    Field('record','integer',label='registro'),
    Field('hmp45c_temp_max','double',label='hmp45c-temp-max'),
    Field('hmp45c_temp_tmx','datetime',label='hmp45c-temp-tmx'),
    Field('hmp45c_temp_min','double',label='hmp45c-temp-min'),
    Field('hmp45c_temp_tmin','datetime',label='hmp45c-temp-tmin'),
    Field('hmp45c_rh_max','double',label='hmp45c-rh-max'),
    Field('hmp45c_rh_tmx','datetime',label='hmp45c-rh-tmx'),
    Field('hmp45c_rh_min','double',label='hmp45c-rh-min'),
    Field('hmp45c_rh_tmn','datetime',label='hmp45c-rh-tmn'),
    Field('rh05103_veloc_max','double',label='rh05103-veloc-max'),
    Field('rh05103_veloc_tmx','datetime',label='rh05103-veloc-tmx'),
    Field('tb4_tot','double',label='tb4_tot')
)

db.define_table('aluno',
     Field('name'),
     Field('sobrenome'))

#lista de campos do baixa 1
baixa1_field=[db.baixa1.dia_hora,db.baixa1.record,db.baixa1.batt_volt_min,db.baixa1.p_temp,db.baixa1.nr_lite_avg,
                db.baixa1.cm3_up_avg,db.baixa1.cm3_dn_avg,db.baixa1.cg3_up_corr_avg,db.baixa1.cg3_dn_corr_avg,
                db.baixa1.cnr1_tc_avg,db.baixa1.cma11_up_avg,db.baixa1.cma11_dn_avg,db.baixa1.li_190s_avg,
                db.baixa1.vw_avg,db.baixa1.hfp01_avg,db.baixa1.stp01_50cm_avg,db.baixa1.stp01_20cm_avg,
                db.baixa1.stp01_10cm_avg,db.baixa1.stp01_05cm_avg,db.baixa1.stp01_02cm_avg,db.baixa1.cs106_avg,
                db.baixa1.hmp45c_temp_avg,db.baixa1.hmp45c_rh_avg,db.baixa1.wind_speed,db.baixa1.win_direction,db.baixa1.tb4_tot]