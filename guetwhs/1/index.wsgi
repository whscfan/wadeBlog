#coding:utf-8
import sae
import haozi.wsgi as ws 
application = sae.create_wsgi_app(ws.application)

