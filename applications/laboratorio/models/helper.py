def is_administrador(id_administrador):
    valor = None
    query1 = db.auth_membership.group_id == 1
    query2 = db.auth_membership.user_id == id_administrador
    dbset = db(query1 & query2)
    if(dbset.select()):
        valor = True
    else:
        valor = False

    return valor

def associated_email(email_usuario):
    valor = False
    emails = db(db.auth_user).select("email")

    for email in emails:
        if email_usuario == email.email:
            valor = True

    return valor

def is_dat(file):
    validator = False
    filename = file['arquivo'].filename
    filename = filename[-4:]
    if filename == ".dat":
        validator = True
    return validator

def check_NAN(list_fields):
    indice = 0
    for value in list_fields:
        if value == "\"NAN\"":
            list_fields[indice] = None
        indice = indice + 1
    return list_fields

def extract_fields(line):
    list_fields = line.split(",")
    list_fields[0] = list_fields[0].replace('"','')
    list_fields = check_NAN(list_fields)
    tam = len(list_fields)
    fields = [tam,list_fields]
    return fields

def is_persisted(dia_hora):
    registro = None
    if db(db.baixa1.dia_hora == dia_hora).select():
        registro = True
    else:
        registro = False
    return registro

def insert_baixa1(lista):
    persistido = is_persisted(lista[0])
    validator = None
    if not persistido:
        validator = db.baixa1.insert(dia_hora = lista[0], record=lista[1], batt_volt_min=lista[2], p_temp=lista[3], nr_lite_avg=lista[4],
                                    cm3_up_avg=lista[5], cm3_dn_avg=lista[6], cg3_up_corr_avg = lista[7], cg3_dn_corr_avg = lista[8], cnr1_tc_avg = lista[9],
                                    cma11_up_avg=lista[10],cma11_dn_avg=lista[11], li_190s_avg=lista[12],vw_avg = lista[13], hfp01_avg=lista[14],
                                    stp01_50cm_avg = lista[15], stp01_20cm_avg = lista[16], stp01_10cm_avg = lista[17], stp01_05cm_avg = lista[18],
                                    stp01_02cm_avg = lista[19], cs106_avg = lista[20], hmp45c_temp_avg = lista[21], hmp45c_rh_avg = lista[22],
                                    wind_speed = lista[23], win_direction = lista[24], tb4_tot = lista[25])
        return validator
    else:
        return False

def process_file(file):
    result = []
    fields = None
    inconsistent_tuples_min = []
    inconsistent_tuples_max = []
    tuplas_not_persisted = []
    lineCounter = 0
    counter_inconsistent_tuples_min = 0
    counter_inconsistent_tuples_max = 0
    counter_tuplas_no_persisted = 0
    counter_tuplas_persisted = 0
    archive = file['arquivo'].file

    for line in archive.readlines():
        if lineCounter < 4:
            lineCounter = lineCounter + 1
        else:
            fields = extract_fields(line)
            list_size = len(fields[1])

            if list_size == 26:
                if not insert_baixa1(fields[1]):
                    counter_tuplas_no_persisted = counter_tuplas_no_persisted + 1
                    tuplas_not_persisted.append(fields[1])
                else:
                    counter_tuplas_persisted = counter_tuplas_persisted + 1
            elif list_size < 26:
                inconsistent_tuples_min.append(fields[1])
                counter_inconsistent_tuples_min = counter_inconsistent_tuples_min + 1
            else:
                inconsistent_tuples_max.append(fields[1])
                counter_inconsistent_tuples_max = counter_inconsistent_tuples_max + 1
            lineCounter = lineCounter + 1

    lineCounter = lineCounter - 4
    result = [lineCounter, counter_tuplas_persisted, counter_tuplas_no_persisted, tuplas_not_persisted,
                counter_inconsistent_tuples_min, inconsistent_tuples_min, counter_inconsistent_tuples_max, inconsistent_tuples_max]
    return result

def extract_fields_baixa2(line):
    list_fields = line.split(",")
    list_fields[0] = list_fields[0].replace('"','')
    list_fields[3] = list_fields[3].replace('"', '')
    list_fields[5] = list_fields[5].replace('"', '')
    list_fields[7] = list_fields[7].replace('"', '')
    list_fields[9] = list_fields[9].replace('"', '')
    list_fields[11] = list_fields[11].replace('"', '')
    list_fields = check_NAN(list_fields)
    tam = len(list_fields)
    fields = [tam,list_fields]
    return fields

def is_persisted_baixa2(dia_hora):
    registro = None
    if db(db.baixa2.dia_hora == dia_hora).select():
        registro = True
    else:
        registro = False
    return registro

def insert_baixa2(lista):
    persistido = is_persisted_baixa2(lista[0])
    validator = None
    if not persistido:
        validator = db.baixa2.insert(dia_hora = lista[0], record=lista[1], hmp45c_temp_max=lista[2], hmp45c_temp_tmx=lista[3], hmp45c_temp_min=lista[4],
                                     hmp45c_temp_tmin=lista[5], hmp45c_rh_max=lista[6], hmp45c_rh_tmx=lista[7], hmp45c_rh_min=lista[8], hmp45c_rh_tmn=lista[9],
                                     rh05103_veloc_max=lista[10],rh05103_veloc_tmx=lista[11], tb4_tot=lista[12])
        return validator
    else:
        return False

def process_file_baixa2(file):
    result = []
    fields = None
    inconsistent_tuples_min = []
    inconsistent_tuples_max = []
    tuplas_not_persisted = []
    lineCounter = 0
    counter_inconsistent_tuples_min = 0
    counter_inconsistent_tuples_max = 0
    counter_tuplas_no_persisted = 0
    counter_tuplas_persisted = 0
    archive = file['arquivo'].file

    for line in archive.readlines():
        if lineCounter < 4:
            lineCounter = lineCounter + 1
        else:
            fields = extract_fields_baixa2(line)
            list_size = len(fields[1])

            if list_size == 13:
                if not insert_baixa2(fields[1]):
                    counter_tuplas_no_persisted = counter_tuplas_no_persisted + 1
                    tuplas_not_persisted.append(fields[1])
                else:
                    counter_tuplas_persisted = counter_tuplas_persisted + 1
            elif list_size < 13:
                inconsistent_tuples_min.append(fields[1])
                counter_inconsistent_tuples_min = counter_inconsistent_tuples_min + 1
            else:
                inconsistent_tuples_max.append(fields[1])
                counter_inconsistent_tuples_max = counter_inconsistent_tuples_max + 1
            lineCounter = lineCounter + 1

    lineCounter = lineCounter - 4
    result = [lineCounter, counter_tuplas_persisted, counter_tuplas_no_persisted, tuplas_not_persisted,
              counter_inconsistent_tuples_min, inconsistent_tuples_min, counter_inconsistent_tuples_max,
              inconsistent_tuples_max]
    return result

def process_data(data):
    if data[0] == '':
        min = db.baixa1.dia_hora.min()
        data[0] = db().select(min).first()[min]

    if data[1] == '':
        max = db.baixa1.dia_hora.max()
        data[1] = db().select(max).first()[max]
    return data

def converte_mes_por_extenso(ano):
    ano_por_extenso = {1:'Janeiro',2:'Fevereiro', 3:'Março',
                       4:'Abril',5:'Maio',6:'Junho',7:'Julho',
                       8:'Agosto',9:'Setembro',10:'Outubro',
                       11:'Novembro',12:'Dezembro'}
    return ano_por_extenso[ano]

#Obtém o menor e maior ano salvos
def get_min_max_years():
    min = db.baixa1.dia_hora.year().min()
    ano_min = db().select(min).first()[min]
    max = db.baixa1.dia_hora.year().max()
    ano_max = db().select(max).first()[max]
    years = {'min':ano_min,'max':ano_max}
    return years

def get_max_date():
    max = db.baixa1.dia_hora.max()
    data_max = db().select(max).first()[max]
    return(data_max)

# Cria o dicionário de disponibilidade de medições
def cria_dic_med():
    dicionario = {}
    for i in range(1,32):
        dicionario[i]=[0,'cal-inativa']
    return dicionario

# Retorna uma lista com a frequência de medições do mês e ano solicitado
def lista_de_disponibilidade(ano,mes):
    lista_dip = cria_dic_med()
    query1 = (db.baixa1.dia_hora.year() == ano) & (db.baixa1.dia_hora.month() == mes)
    verifica = db(query1).isempty()
    if verifica is False:
        for dia in range(1,32):
            query2 = (db.baixa1.dia_hora.year() == ano) & (db.baixa1.dia_hora.month() == mes) & (db.baixa1.dia_hora.day() == dia)
            qtd = int(db(query2).count())
            if (qtd == 0):
                lista_dip[dia][1] = 'cal-vazia'
            elif qtd == 144:
                lista_dip[dia][1] = 'cal-completa'
            else:
                lista_dip[dia][1] = 'cal-incompleta'
            lista_dip[dia][0] = qtd
    return(lista_dip)

def converte_celsius_para_farenheit(temp_celsius):
    temp_farenheit = 1.8*temp_celsius + 32
    return(temp_farenheit)

def converte_farenheit_para_celsius(temp_farenheit):
    temp_celsius = (temp_farenheit - 32)/1.8
    return(temp_celsius)

def get_precipitacao(dia,mes,ano):
    query_data = (db.baixa1.dia_hora.year() == ano)&(db.baixa1.dia_hora.month() == mes)&(db.baixa1.dia_hora.day() == dia)
    total_precipitacao = db(query_data).select(db.baixa1.tb4_tot.sum()).first()[db.baixa1.tb4_tot.sum()]
    return(total_precipitacao)

def get_temp_min(dia,mes,ano):
    query_data = (db.baixa1.dia_hora.year()==ano)&(db.baixa1.dia_hora.month()==mes)&(db.baixa1.dia_hora.day()==dia)
    temp_min = db(query_data).select(db.baixa1.p_temp.min()).first()[db.baixa1.p_temp.min()]
    return(temp_min)

def get_temp_max(dia,mes,ano):
    query_data = (db.baixa1.dia_hora.year()==ano)&(db.baixa1.dia_hora.month()==mes)&(db.baixa1.dia_hora.day()==dia)
    temp_max = db(query_data).select(db.baixa1.p_temp.max()).first()[db.baixa1.p_temp.max()]
    return(temp_max)

def get_wind_speed(dia,mes,ano):
    query_data = (db.baixa1.dia_hora.year() == ano) & (db.baixa1.dia_hora.month() == mes) & (db.baixa1.dia_hora.day() == dia)
    wind_speed = db(query_data).select(db.baixa1.wind_speed.max()).first()[db.baixa1.wind_speed.max()]
    return(wind_speed)

def escala_beaufort(wind_speed):
    classificacao = ""
    if wind_speed >=0 and wind_speed < 0.5:
        classificacao = "Vento Calmo"
    elif wind_speed >= 0.5 and wind_speed <= 1.5:
        classificacao = "Vento Quase Calmo"
    elif wind_speed >= 1.6 and wind_speed <= 2.9:
        classificacao = "Brisa Amena"
    elif wind_speed >= 3.0 and wind_speed <= 5.7:
        classificacao = "Vento Leve"
    elif wind_speed >= 5.8 and wind_speed <= 8.3:
        classificacao = "Vento Moderado"
    elif wind_speed >= 8.4 and wind_speed <= 11.1:
        classificacao = "Vento Forte"
    elif wind_speed >= 11.2 and wind_speed <= 13.9:
        classificacao = "Vento Muito Forte"
    elif wind_speed >= 14 and wind_speed <= 16.6:
        classificacao = "Vento Fortíssimo"
    elif wind_speed >= 16.7 and wind_speed <= 20.9:
        classificacao = "Ventania"
    elif wind_speed >= 21.0 and wind_speed <= 27.8:
        classificacao = "Vendaval"
    elif wind_speed > 27.8:
        classificacao = "Tornado, Furacão"
    else:
        classificacao="Não categorizado!"
    return(classificacao)

def adjustement(ic,temp_celsius,rh,T,R):
    adjustement1=0.0
    adjustement2=0.0
    index_heat = ic
    if rh < 13.0 and (temp_celsius>=26.7 and temp_celsius<=44.4):
        adjustement1 = ((13.0-R)/4)*(((17.0-abs(T-95.0))/17.0)**(1/2))
        index_heat = index_heat - adjustement1
    elif rh >= 85.0 and (temp_celsius>=26.7 and temp_celsius<=30.6):
        adjustement2 = ((R-85.0)/10.0)*((87.0-T)/5.0)
        index_heat = index_heat - adjustement2
    return(index_heat)

def get_hmp45c_temp_max(ano,mes,dia):
    #dia = str((int(dia) + 3))
    query_data = (db.baixa2.dia_hora.year()==ano)&(db.baixa2.dia_hora.month()==mes)&(db.baixa2.dia_hora.day()==dia)
    rows = db(query_data).select()
    row = rows[0]
    temp_max_baixa2 = row.hmp45c_temp_max
    return(temp_max_baixa2)

def get_hmp45c_rh_max(ano,mes,dia):
    # dia = str((int(dia) + 3))
    query_data = (db.baixa2.dia_hora.year() == ano)&(db.baixa2.dia_hora.month() == mes)&(db.baixa2.dia_hora.day()==dia)
    rows = db(query_data).select()
    row = rows[0]
    hmp45c_rh_max = row.hmp45c_rh_max
    return(hmp45c_rh_max)

def index_heat(ano,mes,dia):
    c1 = -42.379
    c2 = 2.04901523
    c3 = 10.14333127
    c4 = -0.22475541
    c5 = -6.83783*(10**(-3))
    c6 = -5.481717*(10**(-2))
    c7 = 1.22874*(10**(-3))
    c8 = 8.5282*(10**(-4))
    c9 = -1.99*(10**(-6))
    temp_celsius = get_hmp45c_temp_max(ano,mes,dia)
    rh = get_hmp45c_rh_max(ano,mes,dia)
    T = converte_celsius_para_farenheit(temp_celsius)
    R = rh/100
    IC = c1 + c2*T + c3*R + c4*T*R + c5*(T**2) + c6*(R**2) + c7*(T**2)*R + c8*T*(R**2) + c9*(T**2)*(R**2)
    index_heat=adjustement(IC,temp_celsius,rh,T,R)
    index_heat = converte_farenheit_para_celsius(index_heat)
    return(index_heat)

def nivel_de_alerta(IC):
    alerta = ""
    if IC >= 0 and IC <= 27:
        alerta = "Não há alerta"
    elif IC >= 27.1 and IC <= 32.0:
        alerta = "Cautela"
    elif IC >= 32.1 and IC <= 41:
        alerta = "Cautela Extrema"
    elif IC >= 41.1 and IC <= 54:
        alerta = "Perigo"
    elif IC > 54.0:
        alerta = "Perigo Extremo"
    else:
        alerta = "Não categorizado"
    return(alerta)

def truncate_number(numero):
    import math
    numeroTruncado = math.floor(numero*10)/10
    return(numeroTruncado)



def formata_dados(dadoNumber):
    dadoString = str(truncate_number(dadoNumber))
    return(dadoString.replace('.',','))

def altera_img_clima(valor):
    if valor == 0:
        regraCSS = "img-sol"
    else:
        regraCSS = "img-chuva"
    return(regraCSS)