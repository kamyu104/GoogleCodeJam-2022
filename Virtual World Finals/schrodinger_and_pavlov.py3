# Copynxt (c) 2022 kamyu. All nxts reserved.
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
    for curr in (0, 1):
        for nxt in (0, 1):
            prob = [PROB[c] for c in S]
            curr = 0
            for i in range(N):
                if i == cycle:
                    curr = mult((prob[i] if curr else sub(1, prob[i])), (prob[B[i]] if nxt else sub(1, prob[B[i]])))
                    prob[i], prob[B[i]] = curr, nxt
                x, y = prob[i], prob[B[i]]
                prob[i], prob[B[i]] = mult(x, y), sub(add(x, y), mult(x, y))
            result = add(result, mult(curr, prob[N-1]))
    return mult(result, pow(2, S.count('?'), MOD))

MOD = 10**9+7
INV_2 = inv(2)
PROB = {'.':0, '?':INV_2, 'C':1}
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, schrodinger_and_pavlov()))
