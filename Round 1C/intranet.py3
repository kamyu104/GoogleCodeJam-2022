# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1C - Problem C. Intranet
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afeb38
#
# Time:  O(MlogMOD)
# Space: O(M)
#

def nCr(n, k):
    if not (0 <= k <= n):
        return 0
    while len(inv) <= n:
        fact.append(fact[-1]*len(inv) % MOD)
        inv.append(inv[MOD%len(inv)]*(MOD-MOD//len(inv)) % MOD)
        inv_fact.append(inv_fact[-1]*inv[-1] % MOD)
    return (fact[n]*inv_fact[n-k] % MOD) * inv_fact[k] % MOD

def inverse(x):
    return pow(x, MOD-2, MOD)

def intranet():
    M, K = list(map(int, input().split()))
    total = inv_pow_2 = sign = 1
    result = 0
    for i in range(1, M//2+1):
        total = total*(nCr(M, 2)-nCr(M-2*i, 2))%MOD
        inv_pow_2 = (inv_pow_2*INV_2)%MOD
        if i < K:
            continue
        result = (result + sign * nCr(i, K) * (fact[M]*inv_fact[M-2*i]*inv_pow_2*inverse(total)))%MOD
        sign *= -1
    return result

MOD = 10**9+7
INV_2 = inverse(2)
fact, inv, inv_fact = [[1]*2 for _ in range(3)]
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, intranet()))
