#-*- coding:utf-8 _*-  
""" 
@author:charlesXu
@file: Viterbi.py 
@desc: 维特比算法
@time: 2018/04/27 
"""

def viterbi(obs, states, start_p, trans_p, emit_p):
    '''

    :param obs: 可见序列
    :param states: 隐状态
    :param start_p: 初始概率
    :param trans_p: 转移概率
    :param emit_p:  观测概率
    :return: 序列 + 概率
    '''
    path = {}  # 路劲
    V = [{}]  # 记录第几次的概率
    for state in states:
        V[0][state] = start_p[state] * emit_p[state].get(obs[0], 0)
        path[state] = [state]

    for n in range(1, len(obs)):
        V.append({})
        newpath = {}
        for k in states:
            pp, pat = max([(V[n - 1][j] * trans_p[j].get(k, 0) * emit_p[k].get(obs[n], 0), j) for j in states])
            V[n][k] = pp
            newpath[k] = path[pat] + [k]
        path = newpath
    (prob, state) = max([(V[len(obs) - 1][y], y) for y in states])
    return state, prob

