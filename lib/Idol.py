import Skill
import CenterSkill
import os

import myjson

class Idol:
    def __init__(self, config, name, music):
        self.skillLevel = 10
        self.name = name

        path = config["baseDir"]+ "idols/"+name+".json"
        if (not os.path.exists(path)):
            path = config["baseDir"]+"/idols.data/"+name+".json"
        idolData = myjson.json2dict(path) #raise exception
        self.nameJp = idolData["name"]
        self.type = idolData["type"]
        self.centerSkill = CenterSkill.CenterSkill(idolData["centerSkill"])
        self.skill = Skill.Skill(self, music, idolData["skill"])

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getNameJp(self):
        return self.nameJp
        
    def getSkillLevel(self):
        return self.skillLevel

    def getSkill(self):
        return self.skill
        
    def getCenterSkill(self):
        return self.centerSkill
