# coding: utf-8
from random import random


def gen_A(k, V):
    A = [None] * (k+1)
    A[0] = V
    A[k] = []
    th = len(V) ** (-1/k)
    for i in range(1, k):
        A[i] = [v for v in A[i-1] if random() < th]
    return A


def gen_rest(k, V, d, A):
    dA = {}
    p = {}
    B = {}
    for v in V:
        for i in range(k):
            dA[i,v] = min(d[w,v] for w in A[i])
            p[i,v] = next(w for w in A[i] if d[w,v] == dA[i,v])
        dA[k,v] = float('inf')
        B[v] = [
            w
            for i in range(k)
            for w in A[i] if w not in A[i+1]
            and d[w,v] < dA[i+1,v]
        ]
    return dA, p, B


def prepro(k, V, d):
    A = [[],[]]
    while not A[-2]:
        A = gen_A(k, V)
    dA, p, B = gen_rest(k, V, d, A)
    return A, dA, p, B


def dist(u, v, B, p, d):
    w = u
    i = 0
    while w not in B[v]:
        i = i+1
        u,v = v,u
        w = p[i,v]
    return d[w,u] + d[w,v], w, i


import itertools

def ex2():
    V = 'abc'
    d = {(a,b): 0 if a == b else
         1 if b == 'b' else
         10000 for a,b in itertools.product(V,V)}

    u,v = 'ab'
    print('d:', {''.join(k): v for k,v in d.items()})
    print('u,v: a,b')
    print('%s  %6s  %15s' % ('dist(u,v)', 'A', 'B'))
    for A1 in 'a', 'ab', 'ac', 'abc', 'b', 'bc', 'c':
        A = [V, A1, '']
        dA, p, B = gen_rest(2, V, d, A)
        Blite = {k: ''.join(v) for k,v in B.items()}
        dst, w, i = dist(u, v, B, p, d)
        print('%5r   %18r   %r' % (dst , A, Blite), w, i)


def ex3():
    V = 'abc'
    d = {(a,b): 0 if a == b else
         1 if b == 'a' else
         10000 for a,b in itertools.product(V,V)}

    u,v = 'ab'
    print('d:', {''.join(k): v for k,v in d.items()})
    print('u,v: a,b')
    print('%s  %6s  %15s' % ('dist(u,v)', 'A', 'B'))
    for A1 in 'a', 'ab', 'ac', 'abc', 'b', 'bc', 'c':
        A = [V, A1, '']
        dA, p, B = gen_rest(2, V, d, A)
        Blite = {k: ''.join(v) for k,v in B.items()}
        print('%5r   %18r   %r' % (dist(u, v, B, p, d) , A, Blite))


