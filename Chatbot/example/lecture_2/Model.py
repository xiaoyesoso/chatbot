#-*- coding:utf-8 _*-  
""" 
@author:charlesXu
@file: Model.py 
@desc: RNN模型层
@time: 2018/02/23 
"""

import logging
import time
import numpy as np
import tensorflow as tf

logging.getLogger('tensorflow').setLevel(logging.WARNING)

class CharRNNLM(object):
    def __init__(self, is_training, batch_size, num_unrollings, vocab_size, hidden_size,
                 max_grad_norm, embedding_size, num_layers, learning_rate, cell_type, dropout=0.0,
                 input_dropout=0.0, infer=False):
        self.batch_size = batch_size
        self.num_unrollings = num_unrollings
        if infer:
            self.batch_size = 1
            self.num_unrollings = 1
        self.hidden_size = hidden_size
        self.vocab_size = vocab_size
        self.max_grad_norm = max_grad_norm
        self.num_layers = num_layers
        self.embedding_size = embedding_size
        self.cell_type = cell_type
        self.dropout = dropout
        self.input_dropout = input_dropout
        if embedding_size <= 0:
            self.input_size = vocab_size
            self.input_dropout = 0.0
        else:
            self.input_size = embedding_size

        self.input_data = tf.placeholder(tf.int64)


        pass
