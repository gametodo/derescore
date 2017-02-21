import codecs
from UnicodeException import UnicodeException

def putFile(path, contents):
    f =codecs.open(path, 'w', 'utf_8')
    if f is None:
        raise UnicodeException(u"putFile File cannot open File:" + path)
    f.write(contents)
    f.close()

def readTsv (path):
    ret = []
    f = codecs.open(path, 'r', 'utf_8')
    if f is None:
        raise UnicodeException(u"readTsv File not found Path:" + path)
    for line in f:
        ret.append(line.replace("\r", "").replace("\n", "").split("\t"))
    f.close()
    return ret

def readCsv (path):
    ret = []
    f = codecs.open(path, 'r', 'utf_8')
    if f is None:
        raise UnicodeException(u"readCsv File not found Path:" + path)
    for line in f:
        ret.append(line.replace("\r", "").replace("\n", "").split(","))
    f.close()
    return ret
    
def readText (path):
    ret = []
    f = codecs.open(path, 'r', 'utf_8')
    if f is None:
        raise UnicodeException(u"readText File not found Path:" + path)
    for line in f:
        ret.append(line.replace("\r", "").replace("\n", ""))
    f.close()
    return ret
