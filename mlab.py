import mongoengine

#
##mongodb://<dbuser>:<dbpassword>@ds129422.mlab.com:29422/baoluong

host = "ds129422.mlab.com"
port = 29422
db_name = "baoluong"
user_name = "admin"
password = "Hai1345678"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())