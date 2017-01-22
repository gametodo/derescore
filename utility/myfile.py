import codecs

def putFile(fname, contents):
    f =codecs.open(fname, 'w', 'utf_8')
    f.write(contents)
    f.close()

# read linux type newline (\n) tsv file
def readTsv (file):
    ret = []
    f = codecs.open(file, 'r', 'utf_8')
    for line in f:
        ret.append(line.replace("\r", "").replace("\n", "").split("\t"))
    f.close()
    return ret

def readCsv (file):
    ret = []
    f = codecs.open(file, 'r', 'utf_8')
    for line in f:
        ret.append(line.replace("\r", "").replace("\n", "").split(","))
    f.close()
    return ret
    
def readText (file):
    ret = []
    f = codecs.open(file, 'r', 'utf_8')
    for line in f:
        ret.append(line.replace("\r", "").replace("\n", ""))
    f.close()
    return ret
