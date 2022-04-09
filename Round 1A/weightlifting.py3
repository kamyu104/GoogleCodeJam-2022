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
    dp = [[0]*E for _ in range(E)]  # dp[i][j]: number of common exercises in [i, j] of X
    for i in range(E):
        curr = [INF]*W
        for j in range(i, E):
            for k in range(W):
                curr[k] = min(curr[k], X[j][k])
            dp[i][j] = sum(curr)
    dp2 = [[INF]*E for _ in range(E)]  # dp2[i][j]: min number of ops in [i, j] of X
    for j in range(E):
        dp2[j][j] = 2*dp[j][j]
        for i in reversed(range(j)):
            for k in range(i, j):
                dp2[i][j] = min(dp2[i][j], dp2[i][k]+dp2[k+1][j]-2*dp[i][j])
    return dp2[0][E-1]

INF = float("inf")
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, weightlifting()))
