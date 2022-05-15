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
    r = N//2
    for r in reversed(range(1, N//2+1)):
        if not remain:
            break
        x = N**2-4*r*(r+1)
        for i in range(4):
            diff = 8*r-2*(i+1)+1
            if diff-1 > remain:
                continue
            remain -= diff-1
            result.append((x+(2*i+1)*r, (x+(2*i+1)*r)+diff))
            break
    return "%s\n%s"% (len(result), "\n".join(map(lambda x: "%s %s"%(x[0], x[1]), result))) if not remain else "IMPOSSIBLE"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, spiraling_into_control()))
