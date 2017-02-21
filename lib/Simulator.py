from collections import OrderedDict
import math

import Unit
import Idol
import Music

class Simulator:
    unit = None
    music = None
    baseScore = None
    def __init__ (self, config, totalApeal, musicName, difficalty, idolNames, calcType):
        self.calcType = calcType
        Simulator.music = Music.Music(config, musicName, difficalty)
        Simulator.baseScore = Simulator.music.getBaseScore(totalApeal)
        Simulator.unit = Unit.Unit([Idol.Idol(config,name, self.music) for name in idolNames])

    def getBaseScore(self):
        return Simulator.baseScore
        
    def init(self):
        self.skillHistory = []
        self.skillHistory2 = []
        self.skillCounter = 0
        self.skillCounterArray = OrderedDict({})
        for idol in Simulator.unit.getIdols():
            self.skillCounterArray[idol.getName()] = 0
        self.score300 = 0
        self.currentNotes = 0
        centerSkill = Simulator.unit.getCenterSkill()
        for idol in Simulator.unit.getIdols():
            idol.getSkill().calcActivationRate(centerSkill, self.calcType)
            idol.getSkill().calcIsActivate()
            
    def calcScore(self):
        score = reduce(lambda score, currentNotes:self._score(score, currentNotes), range(0, Simulator.music.getQuantity()), 0)
        return (score, self.score300, self.unit, self.skillHistory, self.skillHistory2)

    def _log(self, idol, isInvocation):
        self.skillHistory.append("%d, %s, %d"%(self.currentNotes, idol.getName(), isInvocation))

    def _currentSkill(self, idol):
        noteTime = Simulator.music.getNoteTime(self.currentNotes)
        isInvocation = idol.getSkill().isActivateTime(noteTime, 0.0)
        if isInvocation:
            self._log(idol, isInvocation)
            return idol.getSkill().getValue()
        return 1.0

    def _calcSkillRate(self):
        return max([self._currentSkill(idol) for idol in Simulator.unit.getIdols() if idol.getSkill().isScore()])

    def _calcComboRate(self):
        if (self.currentNotes == 0):
            return 1.0
        return max([self._currentSkill(idol) for idol in Simulator.unit.getIdols() if idol.getSkill().isCombo()])

    def _score(self, currentScore, currentNotes):
        self.currentNotes = currentNotes
        if currentNotes == 299:
            self.score300 = currentScore
        comboOdds = Simulator.music.getComboRate(currentNotes)
        skillScore = self._calcSkillRate()
        skillCombo = self._calcComboRate()
        currentPoint = round(Simulator.baseScore * comboOdds * skillScore * skillCombo)
        noteTime = Simulator.music.getNoteTime(currentNotes)
        idols =Simulator.unit.getIdols()
        self.skillHistory2.append("%d, %f, %d, %f, %s"%(currentNotes+1, noteTime, int(currentPoint), comboOdds, ",".join([str(self._currentSkill(idol)) for idol in Simulator.unit.getIdols()])))
        return currentScore + currentPoint
