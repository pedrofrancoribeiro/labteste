# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    if not session.counter:
        session.counter = 1
    else:
        session.counter += 1
    return dict(message="Hello from MyApp", counter=session.counter)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def first():
    documento = request.vars.visitor_name.file
    file = open('myfile.txt','w')
    for linha in documento.readlines():
        lista = linha.split(",")
        file.write(linha)
    file.close()
    redirect(URL('second', vars=dict(name=lista[0])))
    return dict()

def second():
    name = request.vars.name or redirect(URL('terceiro'))
    return dict(name=name)

def terceiro():
    form = FORM(
        INPUT(_name='visitor_name',_type='file', requires=IS_NOT_EMPTY()),
        INPUT(_type='submit')
    )
    if form.process().accepted:
        documento = form.vars.visitor_name.file
        for linha in documento.readlines():
            lista = linha.split(",")
            cont=0
            for palavra in lista:
                if palavra == "\"NAN\"":
                    lista[cont] = "None"
                cont = cont + 1
        redirect(URL('second',vars=dict(name = lista[0])))     
    return dict(form=form)

def quarto():
    form = SQLFORM.factory(
        Field('visitor_name', 'upload',label='what is your name?',requires=IS_NOT_EMPTY()))
    if form.process().accepted:
        documento = form.vars.visitor_name.file
        for linha in documento.readlines():
            lista = linha.split(",")
            cont=0
            for palavra in lista:
                if palavra == "\"NAN\"":
                    lista[cont] = "None"
                cont = cont + 1
        redirect(URL('second',vars=dict(name = lista[0])))
    return dict(form=form)
