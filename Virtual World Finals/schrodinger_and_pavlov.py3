# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Virtual World Finals - Problem D. Schrödinger and Pavlov
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087762e/0000000000b9c73a
#
# Time:  O(N), pass in PyPy3 but Python3
# Space: O(N)
#

def inv(x):
    return pow(x, MOD-2, MOD)

def add(a, b):
    return (a+b)%MOD

def sub(a, b):
    return (a-b)%MOD

def mult(a, b):
    return (a*b)%MOD

def find_cycle(B):
    curr = len(B)-1
    while B[curr] < curr:
        curr = B[curr]
    return curr

def schrodinger_and_pavlov():
    N = int(input())
    S = input()
    B = list(map(lambda x: int(x)-1, input().split()))
    cycle = find_cycle(B)
    result = 0
    for left in (0, 1):
        for right in (0, 1):
            prob = [PROB[c] for c in S]
            curr = 0
            for i in range(N):
                if i == cycle:
                    curr = mult((prob[i] if left else sub(1, prob[i])), (prob[B[i]] if right else sub(1, prob[B[i]])))
                    prob[i], prob[B[i]] = left, right
                prob[i], prob[B[i]] = mult(prob[i], prob[B[i]]), sub(add(prob[i], prob[B[i]]), mult(prob[i], prob[B[i]]))
            result = add(result, mult(curr, prob[N-1]))
    return mult(result, pow(2, S.count('?'), MOD))

MOD = 10**9+7
INV_2 = inv(2)
PROB = {'.':0, '?':INV_2, 'C':1}
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, schrodinger_and_pavlov()))
