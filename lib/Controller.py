import myfile
import Simulator

def sumActivate(idol):
    return len([ 1 for isActivate in idol.getSkill().getActivates() if isActivate])

def simulate(config, inputDict, loopTimes):
    Simulator.unit = None
    Simulator.music = None
    Simulator.baseScore = None
    simulator = Simulator.Simulator(config, inputDict["totalApeal"], inputDict["musicName"], inputDict["difficalty"], inputDict["idolNames"], inputDict["scoreType"])
    scores = []
    sumScores = 0
    for i in range(0,loopTimes):
        simulator.init()
        score, score300, unit, skillHistory, skillHistory2 = simulator.calcScore()
        scores.append(score)
        sumScores = sumScores + score
        # myfile raise exception
        myfile.putFile("output/skill%04d.txt" %(i), "\n".join(skillHistory))
        myfile.putFile("output/vskill%04d.txt" %(i), "\n".join(skillHistory2))

    return (scores, sumScores)
