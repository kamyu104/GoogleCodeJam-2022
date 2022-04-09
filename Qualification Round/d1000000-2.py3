# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Qualification Round - Problem C. d1000000
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a46471
#
# Time:  O(NlogN)
# Space: O(1)
#

def d1000000():
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    result = 0
    for x in S:
        if result+1 <= x:
            result += 1
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, d1000000()))
