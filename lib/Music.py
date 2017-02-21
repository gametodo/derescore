import myjson
import myfile
import math
import os.path

class Music:
    baseScoreRateList = {
        5:1.0, 6:1.025, 7:1.05, 8:1.075, 9:1.1
        ,10:1.2, 11:1.225, 12:1.25, 13:1.275, 14:1.3
        ,15:1.4, 16:1.425, 17:1.45, 18:1.475, 19:1.5
        ,20:1.6, 21:1.65, 22:1.7, 23:1.75, 24:1.8 ,25:1.85
        ,26:1.9, 27:1.95, 28:2.0, 29:2.1, 30:2.2
    }
    
    def __init__(self, config, name, difficalty):
        path = config["baseDir"]+"/musics/"+name+".json"
        if (not os.path.exists(path)):
            path = config["baseDir"]+"/musics.data/"+name+".json"
        musicJson = myjson.json2dict(path) # raise Exception
        self.name = name
        self.difficalty = difficalty
        self.title = musicJson["title"]
        self.length = int(musicJson["length"])
        self.quantity = int(musicJson[difficalty + "Quantity"])
        self.baseScoreRate = self._calcBaseScoreRate(int(musicJson[difficalty+"Lv"]))
        self.type = musicJson["type"]
        self.comboRate = []
        self.calcComboRate()
        notesPath = config["baseDir"]+"/musics/"+name+"-"+difficalty + "-notes.csv"
        if (not os.path.exists(notesPath)):
            notesPath = config["baseDir"]+"/musics.data/"+name+"-"+difficalty + "-notes.csv"
        matrix = myfile.readCsv(notesPath) # raise Exception
        matrix[0].pop(0)
        self.notes = [float(str) for str in matrix[0]]

    def getType(self):
        return self.type

    def getQuantity(self):
        return self.quantity

    def getLength(self):
        return self.length

    def getComboRate(self, currentNotes):
        return self.comboRate[currentNotes]

    def _getBaseScoreRate(self):
        return self.baseScoreRate

    def _calcBaseScoreRate(self, lv):
        return Music.baseScoreRateList[lv]

    def getBaseScore(self, apeal):
        return apeal * self._getBaseScoreRate() / self.getQuantity()

    def calcComboRateConditions(self):
        comboRateConditions = {}
        comboRateConditions[math.floor(self.getQuantity() * 0.9)] = 2
        comboRateConditions[math.floor(self.getQuantity() * 0.8)] = 1.7
        comboRateConditions[math.floor(self.getQuantity() * 0.7)] = 1.5
        comboRateConditions[math.floor(self.getQuantity() * 0.5)] = 1.4
        comboRateConditions[math.floor(self.getQuantity() * 0.25)] = 1.3
        comboRateConditions[math.floor(self.getQuantity() * 0.1)]  = 1.2
        comboRateConditions[math.floor(self.getQuantity() * 0.05)] = 1.1
        comboRateConditions[0] = 1.0
        return comboRateConditions

    def calcComboRate(self):
        comboRateConditions = self.calcComboRateConditions()
        def maxComboRate(currentNotes):
            return max([ comboRateConditions[key] for key in comboRateConditions if key <= currentNotes])
        self.comboRate = map(maxComboRate, range(0, self.getQuantity()))

    def getNoteTime(self, currentNotes):
        return self.notes[currentNotes]

