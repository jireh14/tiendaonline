import web

db_host = 'grp6m5lz95d9exiz.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'y7cjfhg6p993sgr1'
db_user = 'kv0t31z8y9qv3jqf'
db_pw = 'ouiap1hd9skbwdje'

'''db_host = 'localhost'
db_name = 'web_admin'
db_user = 'admin'
db_pw = 'admin.2021''''

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )