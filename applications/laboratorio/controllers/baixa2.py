#coding: utf-8

@auth.requires_login()
@auth.requires_membership("admin")
def inserir():
    mensagem = None
    mensagemClass = None
    resultado = []
    if request.vars:
        file = request.vars
        if is_dat(file):
            resultado = process_file_baixa2(file)
            if resultado[0] == resultado[1]:
                mensagemClass = "alert alert-success alert-dismissable"
                mensagem = "Processo de inserção de dados realizado com sucesso!"
            elif resultado[0] == resultado[2]:
                mensagemClass = "alert alert-danger alert-dismissable"
                mensagem = "Nenhuma tupla persistida"
            else:
                mensagemClass = "alert alert-info alert-dismissable"
                mensagem = "Algumas tuplas podem não ter sido inseridas!"
        else:
            mensagemClass = "alert alert-warning alert-dismissable"
            mensagem = session.auth.users.first_name + "você informou um arquivo com extensão inválida!"
            resultado = [None, None, None, None, None, None, None]
    return dict(mensagem=mensagem,mensagemClass=mensagemClass,resultado=resultado)

@auth.requires_login()
def selecionar():
    return dict()

@auth.requires_login()
@auth.requires_membership("admin")
def apagar():
    return dict()

@auth.requires_login()
def disponibilidade():
    return dict()