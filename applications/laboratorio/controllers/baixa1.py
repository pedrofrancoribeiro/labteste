#coding: utf-8
@auth.requires_login()
def exibir():
	print request.vars
	rows = db((db.baixa1.dia_hora>="2014-12-31 19:00:00")&(db.baixa1.dia_hora<="2014-12-31 19:50:00")).select()


	headers = request.vars.keys()
	fields = request.vars.values()

	# fields = ["dia_hora","record","batt_volt_min","p_temp","nr_lite_avg","cm3_up_avg","cm3_dn_avg",
	# 			"cg3_up_corr_avg","cg3_dn_corr_avg","cnr1_tc_avg","cma11_up_avg","cma11_dn_avg","li_190s_avg",
	# 			"vw_avg","hfp01_avg","stp01_50cm_avg","stp01_20cm_avg","stp01_10cm_avg","stp01_05cm_avg",
	# 			"stp01_02cm_avg","hmp45c_temp_avg","hmp45c_rh_avg","wind_speed","win_direction","tb4_tot"]

	table = TABLE(THEAD(TR(*[B(header) for header in headers])),
			TBODY(*[TR(*[TD(row[field]) for field in fields]) for row in rows]))
	table["_class"]="table table-striped"
	return dict(table=table)

@auth.requires_login()
def exibir2():
	count_registros = 0
	if request.vars['page']:
		data = session.data
		lista_de_chaves = session.lista_de_chaves
		tam_list = len(lista_de_chaves)
		fields = []
		if tam_list == 3:
		    fields = baixa1_field
		else:
			for valor in  lista_de_chaves:
				if type(valor) == int and valor not in [26,27]:
					fields.append(baixa1_field[valor])
		query = db((db.baixa1.dia_hora>=data[0])&(db.baixa1.dia_hora<=data[1]))
		count_registros = db((db.baixa1.dia_hora>=data[0])&(db.baixa1.dia_hora<=data[1])).count()
		table = SQLFORM.grid(query, user_signature=False, create=False, searchable=False, deletable=False, editable=False, details=False,
		paginate=7, sortable = False, csv = True, links_in_grid=False,maxtextlength=15, links_placement= 'both',formstyle='table3cols',fields=fields)
		table.element('.web2py_counter',replace=None)
		table.element('table')['_class'] = 'table table-striped table-condesed show'
		table.elements('a.btn.btn-default')[0]['_class']= 'btn btn-success'
		table.elements('a.btn.btn-default')[1]['_class']= 'btn btn-success'
		table.elements('a.btn.btn-default')[2]['_class']= 'btn btn-success'
		table.elements('a.btn.btn-default')[3]['_class']= 'btn btn-success'
		table.elements('a.btn.btn-default')[4]['_class']= 'btn btn-success'
		table.elements('a.btn.btn-default')[5]['_class']= 'btn btn-success'
		table.elements('a.btn.btn-default')[6]['_class']= 'btn btn-success'	
	elif not request.vars['_export_type']:
		data = process_data([request.vars['26'],request.vars['27']])
		lista_de_chaves = request.vars.keys()
		lista_de_chaves = list(map(int, lista_de_chaves))
		lista_de_chaves.sort()
		tam_list = len(lista_de_chaves)
		fields = []
		if tam_list == 3:
		    fields = baixa1_field
		else:
			for valor in  lista_de_chaves:
				if type(valor) == int and valor not in [26,27]:
					fields.append(baixa1_field[valor])
		query = db((db.baixa1.dia_hora>=data[0])&(db.baixa1.dia_hora<=data[1]))
		count_registros = db((db.baixa1.dia_hora>=data[0])&(db.baixa1.dia_hora<=data[1])).count()
		session.data = data
		session.lista_de_chaves = lista_de_chaves
		table = SQLFORM.grid(query, user_signature=False, create=False, searchable=False, deletable=False, editable=False, details=False,
		paginate=7, sortable = False, csv = True, links_in_grid=False,maxtextlengths={'baixa1.dia_hora':30}, links_placement= 'both',formstyle='divs',fields=fields)
		table.element('.web2py_counter',replace=None)
		table.element('table')['_class'] = 'table table-striped table-condesed show'
		table.elements('a.btn.btn-default')[0]['_class']= 'btn btn-success'
		table.elements('a.btn.btn-default')[1]['_class']= 'btn btn-success'
		table.elements('a.btn.btn-default')[2]['_class']= 'btn btn-success'
		table.elements('a.btn.btn-default')[3]['_class']= 'btn btn-success'
		table.elements('a.btn.btn-default')[4]['_class']= 'btn btn-success'
		table.elements('a.btn.btn-default')[5]['_class']= 'btn btn-success'
		table.elements('a.btn.btn-default')[6]['_class']= 'btn btn-success'
	else:
		data = session.data
		lista_de_chaves = session.lista_de_chaves
		tam_list = len(lista_de_chaves)
		fields = []
		if tam_list == 3:
		    fields = baixa1_field
		else:
			for valor in  lista_de_chaves:
				if type(valor) == int and valor not in [26,27]:
					fields.append(baixa1_field[valor])
		query = db((db.baixa1.dia_hora>=data[0])&(db.baixa1.dia_hora<=data[1]))
		count_registros = db((db.baixa1.dia_hora>=data[0])&(db.baixa1.dia_hora<=data[1])).count()
		session.data = data
		session.lista_de_chaves = lista_de_chaves
		table = SQLFORM.grid(query, user_signature=False, create=False, searchable=False, deletable=False, editable=False, details=False,
		paginate=7, sortable = False, csv = True, links_in_grid=False,maxtextlength=15, links_placement= 'both',formstyle='table3cols',fields=fields)
		table.element('.web2py_counter',replace=None)
		table.element('table')['_class'] = 'table table-striped table-condesed show'
		table.elements('a.btn.btn-default')[0]['_class']= 'btn btn-primary'
		table.elements('a.btn.btn-default')[1]['_class']= 'btn btn-primary'
		table.elements('a.btn.btn-default')[2]['_class']= 'btn btn-primary'
		table.elements('a.btn.btn-default')[3]['_class']= 'btn btn-primary'
		table.elements('a.btn.btn-default')[4]['_class']= 'btn btn-primary'
		table.elements('a.btn.btn-default')[5]['_class']= 'btn btn-primary'
		table.elements('a.btn.btn-default')[6]['_class']= 'btn btn-primary'
	return dict(table=table,count_registros=count_registros)

@auth.requires_login()
@auth.requires_membership("admin")
def inserir():
    mensagem = None
    mensagemClass = None
    resultado = []
    if request.vars:
    	file = request.vars
    	if is_dat(file):
    		resultado = process_file(file)
    		if resultado[0] == resultado[1]:
	    		mensagemClass = "alert alert-success alert-dismissable"
	    		mensagem = "Processo de inserção de dados realizado com sucesso!"
	    	elif resultado[0] == resultado[2]:
	    		mensagemClass ="alert alert-danger alert-dismissable"
	    		mensagem = "Nenhuma tupla persistida!"
	    	else:
	    		if resultado[1] == 0:
		    		mensagemClass = "alert alert-danger alert-dismissable"
		    		mensagem = "Nenhuma tupla persistida!"
		    	else:
		    		mensagemClass = "alert alert-info alert-dismissable"
		    		mensagem = "Algumas tuplas podem não ter sido inseridas!"
    	else:
    		mensagemClass = "alert alert-warning alert-dismissable"
    		mensagem = session.auth.user.first_name + " você informou um arquivo com extensão inválida!"
    		resultado =[None, None, None, None, None, None,None]
    return dict(mensagem=mensagem,mensagemClass=mensagemClass,resultado=resultado)

@auth.requires_login()
def selecionar():
	if request.args:
		function = request.args(0)
	return dict(function=function)

@auth.requires_login()
@auth.requires_membership("admin")
def apagar():
    if request.vars['id']:
        lista = request.vars['id']
        if type(lista) is list:
            for item in lista:
                query_remove = db.baixa1.id == int(item)
                db(query_remove).delete()
        else:
            query_remove = db.baixa1.id == int(lista)
            db(query_remove).delete()
        data = session.data
        lista_de_chaves = session.lista_de_chaves
        lista_de_chaves.sort()
        tam_list = len(lista_de_chaves)
        fields = []
        if tam_list == 3:
            fields = baixa1_field
        else:
            for valor in  lista_de_chaves:
                if type(valor) == int and valor not in [26,27]:
                    fields.append(baixa1_field[valor])
        query = db((db.baixa1.dia_hora>=data[0])&(db.baixa1.dia_hora<=data[1]))
        session.data = data
        session.lista_de_chaves = lista_de_chaves
        table = SQLFORM.grid(query, user_signature=False, create=False, searchable=False, deletable=False, editable=False, details=False,paginate=10, sortable = False, csv = False, links_in_grid=False,maxtextlength=15, links_placement= 'both',formstyle='divs',fields=fields,selectable=lambda ids : redirect(URL('baixa1','apagar',vars=dict(id=ids))))
    elif request.vars['records']:
        lista = request.vars['records']
        if type(lista) is list:
            for item in lista:
                query_remove = db.baixa1.id == int(item)
                db(query_remove).delete()
        else:
            query_remove = db.baixa1.id == int(lista)
            db(query_remove).delete()
        data = session.data
        lista_de_chaves = session.lista_de_chaves
        lista_de_chaves.sort()
        tam_list = len(lista_de_chaves)
        fields = []
        if tam_list == 3:
            fields = baixa1_field
        else:
            for valor in  lista_de_chaves:
                if type(valor) == int and valor not in [26,27]:
                    fields.append(baixa1_field[valor])
        query = db((db.baixa1.dia_hora>=data[0])&(db.baixa1.dia_hora<=data[1]))
        session.data = data
        session.lista_de_chaves = lista_de_chaves
        table = SQLFORM.grid(query, user_signature=False, create=False, searchable=False, deletable=False, editable=False, details=False,paginate=10, sortable = False, csv = False, links_in_grid=False,maxtextlength=15, links_placement= 'both',formstyle='divs',fields=fields,selectable=lambda ids : redirect(URL('baixa1','apagar',vars=dict(id=ids))))
    elif request.vars['page']:
        data = session.data
        lista_de_chaves = session.lista_de_chaves
        tam_list = len(lista_de_chaves)
        fields = []
        if tam_list == 3:
            fields = baixa1_field
        else:
            for valor in  lista_de_chaves:
                if type(valor) == int and valor not in [26,27]:
                    fields.append(baixa1_field[valor])
        query = db((db.baixa1.dia_hora>=data[0])&(db.baixa1.dia_hora<=data[1]))
        table = SQLFORM.grid(query, user_signature=False, create=False, searchable=False, deletable=False, editable=False, details=False,paginate=10, sortable = False, csv = False, links_in_grid=False,maxtextlength=15, links_placement= 'both',formstyle='divs',fields=fields,selectable=lambda ids : redirect(URL('baixa1','apagar',vars=dict(id=ids))))
    else:
        data = process_data([request.vars['26'],request.vars['27']]);
        lista_de_chaves = request.vars.keys()
        lista_de_chaves = list(map(int, lista_de_chaves))
        lista_de_chaves.sort()
        tam_list = len(lista_de_chaves)
        fields = []
        if tam_list == 3:
            fields = baixa1_field
        else :
            for valor in  lista_de_chaves:
                if type(valor) == int and valor not in [26,27]:
                    fields.append(baixa1_field[valor])
        query = db((db.baixa1.dia_hora>=data[0])&(db.baixa1.dia_hora<=data[1]))
        session.data = data
        session.lista_de_chaves = lista_de_chaves
        table = SQLFORM.grid(query, user_signature=False, create=False, searchable=False, deletable=False, editable=False, details=False,paginate=10, sortable = False, csv = False, links_in_grid=False,maxtextlength=15, links_placement= 'both',formstyle='divs',fields=fields,selectable=lambda ids : redirect(URL('baixa1','apagar',vars=dict(id=ids))))
    return dict(table=table)

@auth.requires_login()
def disponibilidade():
    from datetime import datetime
    data_atual = datetime.now()
    years = get_min_max_years()
    if request.vars:
        mes = int(request.vars['cb1-mes'])
        ano = int(request.vars['cb1-ano'])
    else:
        mes = data_atual.month
        ano = data_atual.year
    return dict(ano_minimo=years['min'],ano_maximo=years['max'],mes=mes, ano=ano)

