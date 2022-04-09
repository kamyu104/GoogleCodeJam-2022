# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1A - Problem B. Equal Sum
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa8fc1
#
# Time:  O(N)
# Space: O(1)
#
# python interactive_runner.py python3 testing_tool.py 0 -- python3 equal_sum.py3
#

def write(a):
    print("%s" % " ".join(map(str, a)), flush=True)

def read():
    return list(map(int, input().split()))

def equal_sum():
    N = int(input())
    A_pow2 = [1]
    while len(A_pow2) < N:
        if A_pow2[-1]*2 > MAX_VAL:
            break
        A_pow2.append(A_pow2[-1]*2)
    A_others = []
    i = MAX_VAL
    while len(A_others) < N-len(A_pow2):
        if i&(i-1):  # choose any unused numbers
            A_others.append(i)
        i -= 1
    write(A_pow2+A_others)
    B = read()
    total = (sum(A_pow2)+sum(A_others)+sum(B))//2
    result = []
    for x in A_others+B:
        if x <= total:
            total -= x
            result.append(x)
    assert(total <= MAX_VAL)
    for x in A_pow2:
        if total&x:
            result.append(x)
    write(result)

MAX_VAL = 10**9
for case in range(int(input())):
    equal_sum()
