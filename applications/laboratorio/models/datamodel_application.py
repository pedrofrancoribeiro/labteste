#coding: utf-8
#define os objetos que serão usados em nossa aplicação: Camada de autenticação, de email e webservice

from gluon.tools import Auth,Mail,Service

# Classe de Serviços (WebService)
service = Service()

# Classe de autenticação
auth = Auth(db,hmac_key=Auth.get_or_create_key(),controller="home",function="user")

# para que view o usuário é enviado após o registro
auth.settings.register_next = URL('home','login')

# para que view o usuário é enviado após o login
auth.settings.login_next = URL('home','menu')

# para que view o usuário é enviado após o logout
auth.settings.logout_next = URL('home','index')

auth.messages.label_first_name = 'Nome'
auth.messages.label_last_name = 'Sobrenome'
auth.messages.label_password = 'Senha'


auth.settings.registration_requires_verification = False

# requer que o administrador aprove a solicitação de registro do usuário
auth.settings.registration_requires_approval = False

auth.settings.reset_password_requires_verification = False

mail = Mail()

mail = auth.settings.mailer#quem enviará o email para os usuários
mail.settings.server = config.mail.server
mail.settings.sender = config.mail.sender
mail.settings.login = config.mail.login

auth.define_tables() # criação da tabelas no banco de dados