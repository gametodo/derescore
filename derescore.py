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
inputJson = myjson.json2dict(curDir+"/input.json")

def main(loopTimes):
    try:
        scores, sumScores = Controller.simulate(config, inputJson, loopTimes)
        for score in scores:
            print score
    except UnicodeException as e:
        print e.message
    except Exception as e:
        print "error Exception"
        print e

if len(sys.argv) == 2:
    main(int(sys.argv[1]))
else:
    loopTimes = 1
    main(1)
