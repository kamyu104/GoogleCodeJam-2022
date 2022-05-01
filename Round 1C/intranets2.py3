# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1C - Problem C. Intranets
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afeb38
#
# Time:  precompute: O(MAX_M)
#        runtime:    O(1)
# Space: O(MAX_M)
#

def nCr(n, k):
    return (FACT[n]*INV_FACT[n-k] % MOD) * INV_FACT[k] % MOD

def catalan(n):
    return (FACT[2*n]*INV_FACT[n] % MOD) * INV_FACT[n+1] % MOD

def inv_catalan(n):
    return (INV_FACT[2*n]*FACT[n] % MOD) * FACT[n+1] % MOD

def pow2_mod(x):
    return POW2[x]

def intranets():
    M, K = list(map(int, input().split()))
    p = nCr(M-2, 2*(K-1))*catalan(K-1)*pow2_mod(M-2*K) % MOD
    q = inv_catalan(M-1)
    return p*q % MOD

def precompute():
    while len(INV) <= 2*MAX_M:
        FACT.append(FACT[-1]*len(INV) % MOD)
        INV.append(INV[MOD%len(INV)]*(MOD-MOD//len(INV)) % MOD)
        INV_FACT.append(INV_FACT[-1]*INV[-1] % MOD)
    while len(POW2) <= MAX_M-2:
       POW2.append(POW2[-1]*2 % MOD)

MOD = 10**9+7
FACT, INV, INV_FACT = [[1]*2 for _ in range(3)]
POW2 = [1]
MAX_M = 5*10**5
precompute()
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, intranets()))
