#! /bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import codecs

curDir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curDir + "/utility/")
sys.path.append(curDir + "/lib/")

import Controller
import myjson
from UnicodeException import UnicodeException

config = {}
config["baseDir"] = curDir + "/"
config["configFile"] = curDir + "/config/config.json"
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

def main(loopTimes, inputJson):
    try:
        scores, sumScores = Controller.simulate(config, inputJson, loopTimes)
        for score in scores:
            print score
    except UnicodeException as e:
        print e.message
    except Exception as e:
        print "error Exception"
        print e

if len(sys.argv) > 1:
    inputFileName = sys.argv[1]
    if len(sys.argv) > 2:
        loopTimes = int(sys.argv[2])
    else:
        loopTimes = 1
    inputPath = curDir+"/"+inputFileName
    if not os.path.exists(inputPath):
        raise Exception("file not fond path:" + inputPath)
    inputJson = myjson.json2dict(inputPath)
    main(loopTimes, inputJson)
    
else:
    main(1, curDir+"/input.json")
