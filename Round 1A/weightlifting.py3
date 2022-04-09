# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1A - Problem C. Weightlifting
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa9280
#
# Time:  O(E^2 * W + E^3)
# Space: O(E^2)
#

def weightlifting():
    E, W = list(map(int, input().split()))
    X = [list(map(int, input().split())) for _ in range(E)]
    dp = [[0]*E for _ in range(E)]
    for i in range(E):
        mn = [INF]*W
        for j in range(i, E):
            for k in range(W):
                mn[k] = min(mn[k], X[j][k])
            dp[i][j] += sum(mn)
    dp2 = [[INF]*E for _ in range(E)]
    for i in range(E):
        dp2[i][i] = dp[i][i]
    for r in range(1, E):
        for l in reversed(range(r)):
            for i in range(l, r):
                dp2[l][r] = min(dp2[l][r], dp2[l][i]+dp2[i+1][r]-dp[l][r])
    return dp2[0][E-1]*2

INF = float("inf")
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, weightlifting()))
