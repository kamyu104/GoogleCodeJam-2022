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
    i, l = 1+1, N-1
    while remain and l > 1:
        for j in range(4):
            diff = ((l*4-1)-2*j)
            if diff-1 > remain:
                continue
            remain -= diff-1
            result.append((i+l*j, (i+l*j)+diff))
            break
        i += l*4
        l -= 2
    return "%s\n%s"% (len(result), "\n".join(map(lambda x: "%s %s"%(x[0], x[1]), result))) if not remain else "IMPOSSIBLE"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, spiraling_into_control()))
