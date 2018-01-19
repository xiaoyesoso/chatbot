#-*- coding:utf-8 _*-

"""
@version: 
@author: CharlesXu
@license: Q_S_Y_Q 
@file: Rulebase.py
@time: 2018/1/18 15:54
@desc: 存储和计算一些相似性规则
"""

import os
import json

from gensim.models import word2vec
from gensim import models

class Rules(object):
    def __init__(self, domain, rule_items, children, response, word2vec_model):
        self.id_term = domain
        self.terms = rule_items
        self.model = word2vec_model
        self.response = response
        self.children = children

    def __str__(self):
        res = 'Domain:' + self.id_term
        if self.has_child():
            res += ' with Children:'
            for child in self.children:
                res += ' ' + str(child)
        return res

    if __name__ == '__main__':
        pass