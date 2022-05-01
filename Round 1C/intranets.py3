# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1C - Problem C. Intranets
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afeb38
#
# Time:  O(M * log(MOD))
# Space: O(M)
#

def nCr(n, k):
    if not (0 <= k <= n):
        return 0
    while len(INV) <= n:
        FACT.append(FACT[-1]*len(INV) % MOD)
        INV.append(INV[MOD%len(INV)]*(MOD-MOD//len(INV)) % MOD)
        INV_FACT.append(INV_FACT[-1]*INV[-1] % MOD)
    return (FACT[n]*INV_FACT[n-k] % MOD) * INV_FACT[k] % MOD

def inverse(x):
    return pow(x, MOD-2, MOD)

def intranets():
    M, K = list(map(int, input().split()))
    inv2_pow = total = sign = 1
    result = 0
    for i in range(1, M//2+1):
        inv2_pow = (inv2_pow*INV2) % MOD
        total = (total * (nCr(M, 2)-nCr(M-2*i, 2))) % MOD
        if i < K:
            continue
        result = (result + sign*nCr(i, K)*(FACT[M]*INV_FACT[M-2*i]*inv2_pow*inverse(total))) % MOD  # inclusion-exclusion principle
        sign *= -1
    return result

MOD = 10**9+7
INV2 = inverse(2)
FACT, INV, INV_FACT = [[1]*2 for _ in range(3)]
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, intranets()))
