# -*- coding: utf-8 -*-
routers = dict(
	BASE = dict(
		default_application='laboratorio',
	),
	#app specific router
	laboratorio=dict(
		default_controller='home',
		default_function='index'
	)
)

# rotas em caso de erro
routes_onerror = [
	(r'laboratorio/400',r'/laboratorio/static/fail400.html'),
	(r'laboratorio/403',r'/laboratorio/static/fail403.html'),
	(r'laboratorio/404',r'/laboratorio/static/fail404.html'),
	(r'laboratorio/500',r'/laboratorio/static/fail500.html'),
	(r'*/*',r'/laboratorio/error/index')
]

