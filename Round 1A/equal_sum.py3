# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1A - Problem B. Equal Sum
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa8fc1
#
# Time:  O(NlogN)
# Space: O(N)
#

def write(a):
    print("%s"%" ".join(map(str, a)), flush=True)

def read():
    return list(map(int, input().split()))

def equal_sum():
    N = int(input())
    A = [1]
    while len(A) < N:
        if A[-1]*2 > MAX_A:
            break
        A.append(A[-1]*2)
    A = set(A)
    i = 1
    while len(A) < N:
        if i not in A:
            A.add(i)
        i += 1
    write(A)
    B = read()
    B.sort()
    total = (sum(A)+sum(B))//2
    result = []
    while B and B[-1] <= total:
        result.append(B[-1])
        total -= B.pop()
    base = 1
    while base <= total:
        if total&base:
            result.append(base)
        base <<= 1
    write(result)

MAX_A = 10**9
for case in range(int(input())):
    equal_sum()
