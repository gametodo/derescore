class Unit:
    def __init__(self, idols):
        self.idols = idols

    def getIdols(self):
        return self.idols
        
    def getCenterSkill(self):
        return self.idols[0].getCenterSkill()
