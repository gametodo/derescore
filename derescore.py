# condinf: utf-8
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/utility/")
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/lib/")

import myfile
import myjson
import Simulator
import Skill

curDir = os.getcwd()
config = {}
config["baseDir"] = curDir + "/"
config["configFile"] = curDir + "/conf/kscore-config.json"
totalApeal = 100000
musicName = "toware"
difficalty = "master"
idolNames = ["uduki2", "shoko2", "kaede2", "mayu2", "shiki"]
scoreType = Skill.Skill.FULL

def sumActivate(idol):
    return len([ 1 for isActivate in idol.getSkill().getActivates() if isActivate])

def main(loopTimes):
    simulator = Simulator.Simulator(config, totalApeal, musicName, difficalty, idolNames, scoreType)
    for i in range(0,loopTimes):
        simulator.init()
        score, score300, unit, skillHistory, skillHistory2 = simulator.calcScore()
        activates = map(sumActivate, unit.getIdols())
        print score
        myfile.putFile("output/skill%04d.txt" %(i), "\n".join(skillHistory))
        myfile.putFile("output/vskill%04d.txt" %(i), "\n".join(skillHistory2))

if len(sys.argv) == 2:
    main(int(sys.argv[1]))
else:
    loopTimes = 1
    main(1)
