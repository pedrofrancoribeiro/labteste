#coding: utf-8

# renderizar template
from gluon.template import render
import os

def render_email_cadastro(parametros):
    caminho = os.path.join(request.folder,"views","email_cadastro.html")
    with open(caminho,"r") as template:
        message = render(content=template.read(),context=parametros)
    return message

# página inicial da aplicação
def index():
    return dict()

# página do menu principal da aplicação
@auth.requires_login()
def menu():
    return dict()

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

    if request.args(0) == "not_authorized":
        redirect(URL('static','fail403.html',vars=request.vars))

    if request.args(0) == "login":
        redirect(URL('home','login',vars=request.vars))

    return dict(form=auth())

@auth.requires_login()
def profile():
    #db.auth_user.email.writable = False
    profile = auth.profile()
    return dict(profile=profile)

# página de cadastro do administrador
@auth.requires_login()
@auth.requires_membership("admin")
def cadastrar():
    mensagem = None
    mensagemEmail = None
    mensagemClass = None
    form = SQLFORM(db.auth_user, formstyle="divs")
    if form.process().accepted:

        verificaEnvioEmail = mail.send(
                                to = form.vars.email,
                                subject = "Dados para autenticação LabInstru Web.",
                                message = [None, render_email_cadastro(request.vars)]
                             )

        if verificaEnvioEmail == True:
            mensagemEmail = " Email enviado para " + form.vars.email
            mensagemClass = "alert alert-success alert-dismissable"
        else:
            mensagemEmail = "Porém, não foi possível enviar o email para o usuário"
            mensagemClass = "alert alert-warning alert-dismissable"


        mensagem = "Usuário cadastrado com sucesso!" + mensagemEmail

    elif form.errors:
        mensagemClass = "alert alert-danger alert-dismissable"
        mensagem = form.errors.email

    return dict(form=form,mensagem=mensagem, mensagemClass=mensagemClass)

# página para listar os usuários cadastrados no sistema
@auth.requires_login()
@auth.requires_membership("admin")
def listar():
    users = db(db.auth_user).select()
    count_user = db(db.auth_user).count()

    headers = ["Nome", "Sobrenome", "E-mail", "Editar", "Remover"]
    fields = ["first_name", "last_name", "email", "editar", "remover"]

    table = TABLE()

    thead = THEAD(TR())
    for header in headers:
        thead[0].append(TD(B(header)))
    table.append(thead)

    for user in users:
        tr = TR(_id=user["id"])
        for field in fields:
            if field == "editar":
                link_edit = A(IMG(_src=URL('static/imagens','icone-editar.png'),_class="grow"),_href=URL('home','edit_user',args=user["id"]))
                tr.append(link_edit)
            elif field == "remover":
                link_remove = A(IMG(_src=URL('static/imagens','icone-delete.png'),_class="grow"),_href=URL('home','remove_user',args=user["id"]),  _class='removebutton')
                tr.append(link_remove)
            else:
                tr.append(user[field])
        table.append(tr)

    table["_class"] = "table table-striped table-condensed table-hover"

    return dict(table_users=table,count_user=count_user)

# função para remover o usuário
@auth.requires_login()
@auth.requires_membership("admin")
def remove_user():
    uid = int(request.args(0))
    query = db.auth_user.id == uid
    db(query).delete()
    redirect(URL('home','listar'))
    pass

# página para edição de um usuário
@auth.requires_login()
@auth.requires_membership("admin")
def edit_user():
    uid = int(request.args(0))
    query = db.auth_user.id == uid
    usuario = db(query).select()
    return dict(usuario=usuario)

# função para atualizar um usuário
@auth.requires_login()
@auth.requires_membership("admin")
def update_user():
    if request.vars:
        uid = request.vars.id
        nome = request.vars.first_name
        sobrenome = request.vars.last_name
        email_usuario = request.vars.email

        if not associated_email(email_usuario):
            query = db.auth_user.id == uid
            db(query).update(first_name=nome,last_name=sobrenome,email=email_usuario)
        else:
            print "E-mail já está associado a uma conta válida!"

        redirect(URL('home','listar'))
    pass

def register():
    return dict(register=auth.register())

def retrieve_password():
    return dict(retrieve_password=auth.retrieve_password())

@auth.requires_login()
def change_password():
    change_password = auth.change_password()
    return dict(change_password=change_password)

@auth.requires_login()
def manage_groups():
    return dict(auth_membership=SQLFORM.grid(db.auth_membership))

@auth.requires_login()
@auth.requires_membership('admin')
def manage_users():
    return dict(auth_users=SQLFORM.grid(db.auth_user))

def login():
    mensagem = ""
    if request.post_vars:
        email = request.post_vars['email']
        password = request.post_vars['password']
        if not auth.login_bare(email,password):
            mensagem = "E-mail ou Senha inválido!"
        else:
            redirect(URL('home','menu'))
    return dict(mensagem=mensagem)

@auth.requires_login()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)