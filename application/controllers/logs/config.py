import web
import hmac
import application.models.model_admin
import application.models.model_logs

render = web.template.render('application/views/logs/', base='master')
model = application.models.model_logs
model_admin = application.models.model_admin

secret_key = "admin_key"


def hash_str(s):
    return hmac.new(secret_key, s).hexdigest()


def make_secure_val(s):
    return "%s!%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split('!')[0]
    if h == make_secure_val(val):
        return val
        