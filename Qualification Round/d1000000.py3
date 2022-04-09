# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Qualification Round - Problem C. d1000000
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a46471
#
# Time:  O(MAX_N), pass in PyPy3 but Python3
# Space: O(MAX_N)
#

def inplace_counting_sort(nums, reverse=False):
    count = [0]*(max(nums)+1)
    for num in nums:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i-1]
    for i in reversed(range(len(nums))):
        while nums[i] >= 0:
            count[nums[i]] -= 1
            j = count[nums[i]]
            nums[i], nums[j] = nums[j], ~nums[i]
    for i in range(len(nums)):
        nums[i] = ~nums[i]
    if reverse:
        nums.reverse()

def d1000000():
    N = int(input())
    S = list(map(int, input().split()))
    inplace_counting_sort(S)
    result = 0
    for x in S:
        if result+1 <= x:
            result += 1
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, d1000000()))
