import json
from UnicodeException import UnicodeException

def json2dict(file):
    f = open(file)
    if f is None:
        raise UnicodeException(u"json2dict File not found File:" + file)
    data = json.load(f)
    f.close()
    return data
