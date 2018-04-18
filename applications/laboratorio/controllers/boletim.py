def boletim():
    from datetime import datetime
    data_atual = datetime.now()
    years = get_min_max_years()
    dataMaxima = get_max_date()
    temp_max = 0.0
    temp_min = 0.0
    wind_speed = 0.0
    escala = ""
    indice_calor = 0.0
    alerta_ic = ""
    precipitacao=0.0
    regra_css =""
    if request.vars:
        dia='%02d' % int(request.vars['bol-dia'])
        mes= '%02d' % int(request.vars['bol-mes'])
        ano=int(request.vars['bol-ano'])
    else:
        dia= '%02d' % dataMaxima.day
        mes= '%02d' % dataMaxima.month
        ano=dataMaxima.year
    # Índice de calor
    precipitacao = get_precipitacao(dia, mes, ano)
    regra_css = altera_img_clima(precipitacao)
    precipitacao = formata_dados(precipitacao)
    temp_min = formata_dados(get_temp_min(dia, mes, ano))
    temp_max = formata_dados(get_temp_max(dia, mes, ano))
    wind_speed = get_wind_speed(dia, mes, ano)
    escala = escala_beaufort(wind_speed)
    wind_speed = formata_dados(get_wind_speed(dia, mes, ano))
    indice_calor = index_heat(ano,mes,dia)
    alerta_ic = nivel_de_alerta(indice_calor)
    indice_calor = formata_dados(indice_calor)
    return dict(dia=dia,mes=mes,ano=ano,temp_max=temp_max,temp_min=temp_min,wind_speed=wind_speed, escala=escala, index_heat=indice_calor,alerta_ic=alerta_ic,precipitacao=precipitacao, regra_css=regra_css)