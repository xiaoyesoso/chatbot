#-*- coding:utf-8 _*-  
""" 
@author:charlesXu
@file: Test.py 
@desc:
@time: 2018/04/27 
"""

from  Viterbi import viterbi

'''
26个基本词类标记
（名词n、时间词t、处所词s、方位词f、数词m、量词q、区别词b、代词r、动词v、
形容词a、状态词z、副词d、介词p、连词c、助词u、语气词y、叹词e、拟声词o、
成语i、习惯用语l、简称j、前接成分h、后接成分k、语素g、非语素字x、标点符号w）
'''

state_list = ['Ag', 'a', 'ad', 'an', 'Bg', 'b', 'c', 'Dg',
			  'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l',
			  'Mg', 'm', 'Ng', 'n', 'nr', 'ns', 'nt', 'nx',
			  'nz', 'o', 'p', 'q', 'Rg', 'r', 's','na',
			  'Tg', 't','u', 'Vg', 'v', 'vd', 'vn','vvn',
			  'w', 'Yg', 'y', 'z']

file0 = open('F:\project\chatbot\Chatbot\data\pos-tagging\starts.txt','r')
start_c=eval(file0.read())
file1=open('F:\project\chatbot\Chatbot\data\pos-tagging\emits.txt','r',encoding='utf8')
emit_c=eval(file1.read())
file2=open('F:\project\chatbot\Chatbot\data\pos-tagging//trans.txt','r',encoding='utf8')
trans_c=eval(file2.read())

test_strs=[u"你们 站立 在",
           u"我 站 在 北京 天安门 上 大声 歌唱",
           u"请 大家 坐下 喝茶",
           u"你 的 名字 是 什么",
           u"今天 天气 特别 好"]

for li in range(0, len(test_strs)):
    test_strs[li] = test_strs[li].split()
    for li in test_strs:
        p, out_list = viterbi(li, state_list, start_c, trans_c, emit_c)
        print(li)
        print(out_list)
        print(p)