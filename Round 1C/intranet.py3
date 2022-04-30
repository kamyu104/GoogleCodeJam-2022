# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1C - Problem C. Intranet
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afeb38
#
# Time:  O(M + logMOD)
# Space: O(M)
#

def nCr(n, k):
    while len(inv) <= n:
        fact.append(fact[-1]*len(inv) % MOD)
        inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD)
        inv_fact.append(inv_fact[-1]*inv[-1] % MOD)
    return (fact[n]*inv_fact[n-k] % MOD) * inv_fact[k] % MOD

def inverse(x):
    return pow(x, MOD-2, MOD)

def catalan(n):
    return (nCr(2*n, n)*inverse(n+1)) % MOD

def intranet():
    M, K = list(map(int, input().split()))
    M -= 1
    K -= 1
    p = nCr(M-1, 2*K)*catalan(K)*pow(2, (M-1)-2*K, MOD) % MOD
    q = catalan(M)
    return p*inverse(q) % MOD

MOD = 10**9+7
fact, inv, inv_fact = [[1]*2 for _ in range(3)]
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, intranet()))
