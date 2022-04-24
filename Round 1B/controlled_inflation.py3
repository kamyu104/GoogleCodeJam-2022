# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1B - Problem B. Controlled Inflation
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000accfdb
#
# Time:  O(N * P)
# Space: O(1)
#

from collections import defaultdict

def solution():
    N, P = list(map(int, input().split()))
    X = [list(map(int, input().split())) for _ in range(N)]
    dp = {0:0}
    for x in X:
        a, b = min(x), max(x)
        new_dp = defaultdict(lambda:float("inf"))
        for c, v in dp.items():
            new_dp[a] = min(new_dp[a], v+abs(c-b)+abs(b-a))
            new_dp[b] = min(new_dp[b], v+abs(c-a)+abs(a-b))
        dp = new_dp
    return min(dp.values())

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, solution()))
