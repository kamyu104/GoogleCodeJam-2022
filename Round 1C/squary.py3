# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1C - Problem B. Squary
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afdf76
#
# Time:  O(N)
# Space: O(1)
#

def pair_sum(total, total_square):
    return (total**2-total_square)//2

def squary():
    N, K = list(map(int, input().split()))
    E = list(map(int, input().split()))
    total_square = sum(x**2 for x in E)
    if total_square == 0:
        return 0
    total = sum(E)
    total_pair = pair_sum(total, total_square)
    if total and -total_pair%total == 0:
        return -total_pair//total
    return "%s %s" % (1-total, -pair_sum(1, (total_square+(1-total)**2))) if K >= 2 else "IMPOSSIBLE"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, squary()))
