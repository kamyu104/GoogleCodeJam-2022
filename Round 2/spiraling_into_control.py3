# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 2 - Problem A. Spiraling Into Control
# https://codingcompetitions.withgoogle.com/codejam/round/00000000008778ec/0000000000b15a74
#
# Time:  O(N)
# Space: O(1)
#

def spiraling_into_control():
    N, K = list(map(int, input().split()))
    remain = (N**2-1)-K
    result = []
    for r in reversed(range(1, N//2+1)):
        x = N**2-(2*r+1)**2+1
        for i in range(4):
            diff = (8*r-1)-2*i
            if diff-1 > remain:
                continue
            remain -= diff-1
            y = (x+r)+(2*r)*i
            result.append((y, y+diff))
            break
        if remain <= 1:
            break
    return "%s\n%s"% (len(result), "\n".join(map(lambda x: "%s %s"%(x[0], x[1]), result))) if not remain else "IMPOSSIBLE"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, spiraling_into_control()))
