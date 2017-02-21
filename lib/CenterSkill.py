# -*- coding: utf-8 -*-
import re
from UnicodeException import UnicodeException

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

    def __init__(self, ustr):
        pat = re.compile(CenterSkill.regex, re.X)
        group = pat.search(ustr)
        if not group:
            raise UnicodeException(u"CenterSkill::init fail :" + ustr)
        self.type = CenterSkill.regResultType[group.group(1)]
        self.attribute = CenterSkill.regResultAttribute[group.group(2)]
        self.value = float(group.group(3)) / 100.0

    def getType(self):
        return self.type

    def getAttribute(self):
        return self.attribute

    def getValue(self):
        return self.value
    
    def getAdditionalActivationRate(self):
        return 0.0
