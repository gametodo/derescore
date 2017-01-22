# -*- coding: utf-8 -*-
import re

class CenterSkill:
    regex = ur"""
    ^(3タイプ全てのアイドル編成時、全員の|キュートアイドルの|クールアイドルの|パッションアイドルの)
    (全|ボーカル|ダンス|ビジュアル)アピール値
    (\d+)%アップ"""

    regResultType = {
        u"3タイプ全てのアイドル編成時、全員の" : "tri",
        u"キュートアイドルの" : "cute",
        u"クールアイドルの" : "cool",
        u"パッションアイドルの":"passion"
    }

    regResultAttribute = {
        u"全" : "all",
        u"ボーカル" : "Vo",
        u"ダンス": "Da",
        u"ビジュアル": "Vi"
    }

    def __init__(self, str):
        pat = re.compile(CenterSkill.regex, re.X)
        group = pat.search(str)
        if not group:
            raise Exception("CenterSkill::init fail :" + str)
        self.type = CenterSkill.regResultType[group.group(1)]
        self.attribute = CenterSkill.regResultAttribute[group.group(2)]
        self.effect = float(group.group(3)) / 100.0

    def getType(self):
        return self.type

    def getAttribute(self):
        return self.attribute

    def getEffect(self):
        return self.effect
    
    def getAdditionalActivationRate(self):
        return 0.0
