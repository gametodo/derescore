# -*- coding: utf-8 -*-
import random
import math
import re
import codecs
import sys

## test
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

class Skill:
    FULL = "full"
    PROB = "prob"
    # use re.compile(pat, re.VERBOSE)
    # wiki に合わせてある
    regexs = {
        "score" : (
            {"scrappingLife": None,
             "frequency" : 1,
             "activationRate_jp" : 2,
             "effectTime_jp" : 3,
             "hitType": 4,
             "effect": 5,
             "life": None,
            },
            ur"""
        ^(\d+)秒(?:毎|ごと|間)、
        (高確率|中確率|低確率)で
        (一瞬の間|わずかな間|少しの間|しばらくの?間|かなりの間)[、。]
        ([A-Z/]+)のスコアが?(\d+)[%％]アップ$"""),
        
        "enhance" : (
            {"scrappingLife": None,
             "frequency" : 1,
             "activationRate_jp" : 2,
             "effectTime_jp" : 3,
             "hitType": 4,
             "effect": 5,
             "life": None,
            }, ur"""
        ^(\d+)秒(?:毎|ごと|間)、
        (高確率|中確率|低確率)で
        (一瞬の間|わずかな間|少しの間|しばらくの?間|かなりの間)[、。]
        ([A-Z/]+)をPERFECTにする$"""),
        
        "combo" : (
            {"scrappingLife": None,
             "frequency" : 1,
             "activationRate_jp" : 2,
             "effectTime_jp" : 3,
             "hitType": None,
             "effect": 4,
             "life": None,
            }, ur"""
        ^(\d+)秒(?:毎|ごと|間)、
        (高確率|中確率|低確率)で
        (一瞬の間|わずかな間|少しの間|しばらくの?間|かなりの間)[、。]
        COMBOボーナス(\d+)[%％]アップ$"""),

        "continue" : (
            {"scrappingLife": None,
             "frequency" : 1,
             "activationRate_jp" : 2,
             "effectTime_jp" : 3,
             "hitType": 4,
             "effect": None,
             "life": None,
            }, ur"""
        ^(\d+)秒(?:毎|ごと|間)、
        (高確率|中確率|低確率)で
        (一瞬の間|わずかな間|少しの間|しばらくの?間|かなりの間)[、。]
        ([A-Z/]+)でもCOMBOが継続する"""),

        "rivival": (
            {"scrappingLife": None,
             "frequency" : 1,
             "activationRate_jp" : 2,
             "effectTime_jp" : 3,
             "hitType": None,
             "effect": None,
             "life": 4,
            }, ur"""
        ^(\d+)秒(?:毎|ごと|間)、
        (高確率|中確率|低確率)で
        (一瞬の間|わずかな間|少しの間|しばらくの?間|かなりの間)[、。]?
        PERFECTでライフ(\d+)回復"""),

        "guard": (
            {"scrappingLife": None,
             "frequency" : 1,
             "activationRate_jp" : 2,
             "effectTime_jp" : 3,
             "hitType": None,
             "effect": None,
             "life": None,
            }, ur"""
        ^(\d+)秒(?:毎|ごと|間)、
        (高確率|中確率|低確率)で
        (一瞬の間|わずかな間|少しの間|しばらくの?間|かなりの間)[、。]
        ライフが減少しなくなる"""),

        "overload": (
            {"scrappingLife": 3,
             "frequency" : 1,
             "activationRate_jp" : 2,
             "effectTime_jp" : 4,
             "hitType": 6,
             "effect": 5,
             "life": None,
            }, ur"""
        ^(\d+)秒(?:毎|ごと|間)、
        (高確率|中確率|低確率)でライフを(\d+)消費し、
        (一瞬の間|わずかな間|少しの間|しばらくの?間|かなりの間)
        PERFECTのスコア(\d+)[%％]アップ[、。]
        ([A-Z/]+)でもCOMBO継続$""")
    }
    activationRateJpList = {u"高確率": 0.40, u"中確率": 0.35, u"低確率": 0.30}
    effectTimeJpList = {u"かなりの間": 6.00, u"しばらくの間": 5.00, u"少しの間": 4.00, u"わずかな間": 3.00, u"一瞬の間": 2.00}
       
    def __init__(self, idol, music, skillstr):
        self.music = music
        self.idol = idol
        skillList = self._parseSkillString(skillstr)
        self.type = skillList["type"]
        self.frequency = int(skillList["frequency"])
        self.effectTime = self._calcEffectTime(skillList["effectTime_jp"])
        if skillList["effect"]:
            self.effect = 1.0+ float(skillList["effect"])/100
        else:
            self.effect = 1.0
        self.activationRate_jp = skillList["activationRate_jp"]
        self.isActivateList = []

    def __str__(self):
        return "Skill(type=" + str(self.type) + ", frequency=" + str(self.frequency) + ", effectTime=" + str(self.effectTime) + ", effect="+str(self.effect)+")"

    def isCombo(self):
        return self.type == "combo"

    def isScore(self):
        return self.type == "score" or self.type == "overload"

    def getEffect(self):
        return self.effect
        
    def _groupToList(self, group, fetchers):
        ret = {}
        for name in fetchers:
            if fetchers[name]:
                ret[name] = group.group(fetchers[name])
            else:
                ret[name] = None
        return ret
        
    def _parseSkillString(self, skillstr):
        for key in Skill.regexs:
            fetchers, regex = Skill.regexs[key]
            pat = re.compile(regex, re.X)
            group = pat.search(skillstr)
            if group:
                skillList = self._groupToList(group, fetchers)
                skillList["type"] = key
                return skillList
        raise Exception('Skill::parse fail : ' + skillstr)
        
    def calcActivationRate(self, centerSkill, calcType):
        if calcType == Skill.FULL:
            self.activationRate = 1.0
            return self.activationRate

        additional = 1.0
        if self.idol.getType() == self.music.getType():
            additional = additional + 0.3
        additional = additional + centerSkill.getAdditionalActivationRate()
        return Skill.activationRateJpList[activationRate_jp] * (1 + 0.0555* (self.idol.getSkillLevel() -1 )) * additional

    def _calcEffectTime(self, effectTime_jp):
        lv1 = Skill.effectTimeJpList[effectTime_jp]
        return lv1 + math.floor(lv1 * 5.55) / float(100) * float(self.idol.getSkillLevel() -1 )

    def calcIsActivate(self):
        length = self.music.getLength()
        for i in range(0, int(math.ceil((length - self.frequency) / self.frequency))+1):
            self.isActivateList.append(self._isActivate())

    def _isActivate(self):
        return random.random() < self.activationRate

    def getActivate(self, i):
        try:
            val = self.isActivateList[i]
            return val
        except:
            return False

    def getActivates(self):
        return self.isActivateList
            
    def getActivateCount(self):
        return len(filter(lambda x: x,  self.isActivateList))
            
    def calcNthSkill(self, noteTimeOriginal, tolerance):
        noteTime = noteTimeOriginal + tolerance - self.frequency
        if noteTime < 0:
            return None
        end = self.music.getLength() -3
        if (noteTimeOriginal > end):
            return None
        if (noteTime % self.frequency) > self.effectTime:
            return None
        return int(math.floor(noteTime / self.frequency))
    
    def isActivateTime(self, noteTime, tolerance):
        nth = self.calcNthSkill(noteTime, tolerance)
        if nth is None:
            return False
        return self.getActivate(nth)
