# condinf: utf-8
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/utility/")
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/lib/")

import Controller
import myjson

curDir = os.getcwd()
config = {}
config["baseDir"] = curDir + "/"
config["configFile"] = curDir + "/conf/kscore-config.json"

inputJson = myjson.json2dict(curDir+"/input.json")

def main(loopTimes):
    scores, sumScores = Controller.simulate(config, inputJson, loopTimes)
    for score in scores:
        print score

if len(sys.argv) == 2:
    main(int(sys.argv[1]))
else:
    loopTimes = 1
    main(1)
