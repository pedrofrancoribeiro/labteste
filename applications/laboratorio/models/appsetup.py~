#coding: utf-8
#local onde criamos configurações básicas de nossa aplicação

from gluon.storage import Storage

#cria objeto de configuração da aplicação com storage, evitando assim erros para objetos null
config = Storage(
	db = Storage(),
	mail = Storage(),
	auth = Storage()
)

#define settings para db
config.db.uri = 'mysql://root:root@localhost/dblabinstru'
config.db.pool_size = 10
config.db.check_reserved = ["all"]
config.db.migrate_enabled = True # IMPORTANTE: desabilitar essa opção (False) quando for colocar em produção

#define settings para mail
config.mail.server = 'smtp.gmail.com:587'
config.mail.login = 'labinstru2017@gmail.com:labinstruueaest2017'
config.mail.sender = 'labinstru2017@gmail.com'


#criar/importar funções globais

#habilitar views genericas
response.generic_patterns = ['*']
