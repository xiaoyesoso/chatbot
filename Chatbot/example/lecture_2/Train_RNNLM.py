#-*- coding:utf-8 _*-  
""" 
@author:charlesXu
@file: Train_RNNLM.py 
@desc: 训练RNN语言模型
@time: 2018/02/23 
"""

import numpy as np
import tensorflow as tf
from Model import CharRNNLM
from Utils import VocabularyLoader, batch2string

'''
 1,词语的embedding
 2,embedding空间和state空间
 3,连续词语之间的关联
'''


class BatchGenerator(object):
    def __init__(self, tensor_in, tensor_out, batch_size, seq_length):
        '''
          初始化batch产生器
        :param tensor_in:
        :param tensor_out:
        :param batch_size: 每一个mini-batch里面有多少样本
        :param seq_length: 每一个样本的长度，和batch_size一起决定了每个minibatch的数据量
        '''
        self.batch_size = batch_size
        self.seq_length = seq_length
        
        self.tensor_in = tensor_in
        self.tensor_out = tensor_out
        
        self.create_batches()
        self.reset_batch_pointer()

    def create_batches(self):
        self.num_batches = int(self.tensor_in.size / (self.batch_size * self.seq_length))
        self.tensor_in
        pass

    def reset_batch_pointer(self):
        self.pointer = 0


