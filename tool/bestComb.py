import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../utility/")
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../lib/")

import Controller
import Skill
import myjson

skills = ["04h0",
#          "06m1",
#          "07h1",
          "07m2",
#          "09h2",
          "09m3",
#          "11h3",
          "11m4"
#          "13h4"
]
curDir = os.getcwd()
config = {}
config["baseDir"] = curDir + "/"
config["configFile"] = curDir + "/conf/kscore-config.json"

inputJson = myjson.json2dict(curDir+"/tool/input.json")
inputJson["skillType"] = Skill.Skill.PROB

def makeIdolName (idolType, skillType, typestr):
    return idolType + skillType + typestr

units = [ [makeIdolName("c", cute1, "c18"),
           makeIdolName("c", cute2, "s17"),
           makeIdolName("c", cute3, "o18"),
           makeIdolName("l", cool, "c18"),
           makeIdolName("p", passion, "c18")]
          for cute1 in skills
          for cute2 in skills
          for cute3 in skills
          for cool  in skills
          for passion in skills
          if cute2 != cute3 and cute1 != cool and cute1 != passion and cool != passion]

loopTimes = 1

for idolNames in units:
    inputJson["idolNames"] = idolNames
    scores, sumScores= Controller.simulate(config, inputJson, loopTimes)
    sys.stdout.write(str(sumScores/loopTimes) + "\t")
    print "\t".join(idolNames)
