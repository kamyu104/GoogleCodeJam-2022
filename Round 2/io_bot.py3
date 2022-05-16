# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 2 - Problem D. I, O Bot
# https://codingcompetitions.withgoogle.com/codejam/round/00000000008778ec/0000000000b15167
#
# Time:  O(NlogN)
# Space: O(N)
#

from collections import defaultdict

def cost(a, C):  # Time: O(N)
    cnt, prefix = [[0]*2 for _ in range(2)]
    dp = [0]*2
    lookup = defaultdict(lambda:(0, [0]*2))
    prev = -1
    for i, (x, s) in enumerate(a, 1):
        cnt[s] += 1
        prefix[s] += x
        if s != prev:
            dp[i%2] = dp[(i-2)%2]+2*x  # given dp[-1] = 0
        else:
            dp_j, prefix_j = lookup[cnt[0]-cnt[1]]
            dp[i%2] = min(dp[(i-2)%2]+2*x+C, dp_j+2*(prefix[s]-prefix_j[s]))
        lookup[cnt[0]-cnt[1]] = (dp[i%2], prefix[:])
        prev = s
    return dp[len(a)%2]

def io_bot():
    N, C = list(map(int, input().split()))
    a, b = [], []
    for _ in range(N):
        X, S = list(map(int, input().split()))
        if X > 0:
            a.append((X, S))
        else:
            b.append((-X, S))
    a.sort()
    b.sort()
    return cost(a, C)+cost(b, C)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, io_bot()))
