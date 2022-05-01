# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1C - Problem C. Intranets
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afeb38
#
# Time:  precompute: O(M)
#        runtime:    O(1)
# Space: O(M)
#

def lazy_init(n):
    while len(inv) <= n:
        fact.append(fact[-1]*len(inv) % MOD)
        inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD)
        inv_fact.append(inv_fact[-1]*inv[-1] % MOD)

def nCr(n, k):
    lazy_init(n)
    return (fact[n]*inv_fact[n-k] % MOD) * inv_fact[k] % MOD

def catalan(n):
    lazy_init(2*n)
    return (fact[2*n]*inv_fact[n] % MOD) * inv_fact[n+1] % MOD

def inv_catalan(n):
    lazy_init(2*n)
    return (inv_fact[2*n]*fact[n] % MOD) * fact[n+1] % MOD

def pow2_mod(x):
    while x >= len(pow2):
        pow2.append(pow2[-1]*2 % MOD)
    return pow2[x]

def intranets():
    M, K = list(map(int, input().split()))
    M -= 1
    K -= 1
    p = nCr(M-1, 2*K)*catalan(K)*pow2_mod((M-1)-2*K) % MOD
    q = inv_catalan(M)
    return p*q % MOD

MOD = 10**9+7
fact, inv, inv_fact = [[1]*2 for _ in range(3)]
pow2 = [1]
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, intranets()))
