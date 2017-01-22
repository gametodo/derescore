import json

def json2dict(file):
    f = open(file)
    data = json.load(f)
    f.close()
    return data
