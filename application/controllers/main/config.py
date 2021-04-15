import web
import application.models.model_admin
import application.models.model_logs

#import application.models.model_main

render = web.template.render('application/views/main/', base='master')
model = application.models.model_admin
model_logs = application.models.model_logs

secret_key = "admin_key"
#model = application.models.model_main
    