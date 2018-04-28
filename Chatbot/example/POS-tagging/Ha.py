#-*- coding:utf-8 _*-  
""" 
@author:charlesXu
@file: Ha.py 
@desc: 根据原始数据生成初始状态矩阵，转移概率矩阵和观测矩阵
@time: 2018/04/26 
"""

import sys


'''
（名词n、时间词t、处所词s、方位词f、数词m、量词q、区别词b、代词r、动词v、
形容词a、状态词z、副词d、介词p、连词c、助词u、语气词y、叹词e、拟声词o、
成语i、习惯用语l、简称j、前接成分h、后接成分k、语素g、非语素字x、标点符号w）
'''

start_c = {} # 初始概率
transport_c = {}  # 转移概率
emit_c = {}    # 观测概率
Count_dic = {} # 一个属性下的所有单词，为了求解emit
state_list = ['Ag', 'a', 'ad', 'an', 'Bg', 'b', 'c', 'Dg',
			  'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l',
			  'Mg', 'm', 'Ng', 'n', 'nr', 'ns', 'nt', 'nx',
			  'nz', 'o', 'p', 'q', 'Rg', 'r', 's','na',
			  'Tg', 't','u', 'Vg', 'v', 'vd', 'vn','vvn',
			  'w', 'Yg', 'y', 'z']

lineCount = -1 # 句子总数，为了求出开始概率
for stage0 in state_list:
    transport_c[stage0] = {}
    for stage1 in state_list:
        transport_c[stage0][stage1] = 0.0
    emit_c[stage0] = {}
    start_c[stage0] = 0.0
vocabs = []
classify = []
class_count = {}
for state in state_list:
    class_count[state] = 0.0

with open('F:\project\chatbot\Chatbot\data\pos-tagging\corpus_POS.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        lineCount += 1
        words = line.split(" ")
        for word in words:
            position = word.index('/')
            if '[' in word and ']' in word:
                vocabs.append(word[1:position])
                vocabs.append(word[position+1 : -1])
                break
            if '[' in word:
                vocabs.append(word[1:position])
                classify.append(word[position + 1:])
                break
            if ']' in word:
                vocabs.append(word[:position])
                classify.append(word[position + 1:-1])
                break
            vocabs.append(word[:position])
            classify.append(word[position + 1:])

        if len(vocabs) != len(classify):
            print('词汇数量与类别数量不一致')
            break
        else:
            for n in range(0, len(vocabs)):
                class_count[classify[n]] += 1.0
                if vocabs[n] in emit_c[classify[n]]:
                    emit_c[classify[n]][vocabs[n]] += 1.0
                else:
                    emit_c[classify[n]][vocabs[n]] = 1.0
                if n == 0:
                    start_c[classify[n]] += 1.0
                else:
                    transport_c[classify[n-1]][classify[n]] += 1.0
        vocabs = []
        classify = []

for state in state_list:
    start_c[state] = start_c[state] * 1.0 / lineCount
    for li in emit_c[state]:
        emit_c[state][li] = emit_c[state][li] / class_count[state]
    for li in transport_c[state]:
        transport_c[state][li] = transport_c[state][li] / class_count[state]

file0=open('F:\project\chatbot\Chatbot\data\pos-tagging\starts.txt','w',encoding='utf8')
file0.write(str(start_c))
file1=open('F:\project\chatbot\Chatbot\data\pos-tagging\\trans.txt','w',encoding='utf8')
file1.write(str(transport_c))
file2=open('F:\project\chatbot\Chatbot\data\pos-tagging\emits.txt','w',encoding='utf8')
file2.write(str(emit_c))
file0.close()
file1.close()
file2.close()