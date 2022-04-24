# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1B - Problem A. Pancake Deque
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd59d
#
# Time:  O(N)
# Space: O(1)
#

def solution():
    N = int(input())
    D = list(map(int, input().split()))
    result = curr = 0
    left, right = 0, N-1
    while left <= right:
        if D[left] <= D[right]:
            i = left
            left += 1
        else:
            i = right
            right -= 1
        if D[i] >= curr:
            curr = D[i]
            result += 1
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, solution()))
