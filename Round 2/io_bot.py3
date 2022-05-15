# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 2 - Problem D. I, O Bot
# https://codingcompetitions.withgoogle.com/codejam/round/00000000008778ec/0000000000b15167
#
# Time:  O(NlogN)
# Space: O(N)
#

def DP(a, C):
    if not a:
        return 0
    cnt = [0]*2
    dp = [0]*(len(a)+1)
    lookup = {}
    prefix = [[0] for _ in range(2)]
    for i in range(len(a)):
        for j in range(2):
            prefix[j].append(prefix[j][-1]+(a[i][0] if a[i][1] == j else 0))
    cnt[a[0][1]] += 1
    dp[1] = 2*a[0][0]
    lookup[cnt[0]-cnt[1]] = 1
    for i in range(2, len(dp)):
        cnt[a[i-1][1]] += 1
        if a[i-1][1] != a[i-2][1]:
            dp[i] = dp[i-2]+2*a[i-1][0]
        else:
            j = lookup[cnt[0]-cnt[1]] if cnt[0]-cnt[1] in lookup else 0
            dp[i] = min(dp[i-2]+2*a[i-1][0]+C, dp[j]+2*(prefix[a[i-1][1]][i]-prefix[a[i-1][1]][j]))
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
    return DP(a, C)+DP(b, C)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, io_bot()))
