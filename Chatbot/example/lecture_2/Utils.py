#-*- coding:utf-8 _*-  
""" 
@author:charlesXu
@file: Utils.py 
@desc: RNN训练工具类
@time: 2018/02/23 
"""

import codecs
import json
import numpy as np

class VocabularyLoader(object):
    def load_vocab(self, vocab_file, encoding):
        pass

class BatchGenerator(object):
    def __init__(self):
        pass


def batch2string(batch, index_vocab_dict):
    return ''.join(list(map(index_vocab_dict.get, batch)))


