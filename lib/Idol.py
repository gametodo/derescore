import Skill
import CenterSkill

import myjson

class Idol:
    def __init__(self, config, name, music):
        self.skillLevel = 10
        self.name = name
        idolData = myjson.json2dict(config["baseDir"]+ "idols/"+name+".json")
        self.nameJp = idolData["name"]
        self.type = idolData["type"]
        self.centerSkill = CenterSkill.CenterSkill(idolData["centerSkill"])
        self.skill = Skill.Skill(self, music, idolData["skill"])

    def getName(self):
        return self.name

    def getNameJp(self):
        return self.nameJp
        
    def getSkillLevel(self):
        return self.skillLevel

    def getSkill(self):
        return self.skill
        
    def getCenterSkill(self):
        return self.centerSkill