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
    cnt = [0]*2
    dp = [0]*(len(a)+1)
    lookup = defaultdict(int)
    prefix = [[0] for _ in range(2)]
    for i, p in enumerate(prefix):
        for x, s in a:
            p.append(p[-1]+(x if s == i else 0))
    for i in range(1, len(dp)):
        cnt[a[i-1][1]] += 1
        if i == 1 or a[i-1][1] != a[i-2][1]:
            dp[i] = dp[i-2]+2*a[i-1][0]  # given dp[-1] = 0
        else:
            dp[i] = min(dp[i-2]+2*a[i-1][0]+C, dp[lookup[cnt[0]-cnt[1]]]+2*(prefix[a[i-1][1]][i]-prefix[a[i-1][1]][lookup[cnt[0]-cnt[1]]]))
        lookup[cnt[0]-cnt[1]] = i
    return dp[-1]

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
