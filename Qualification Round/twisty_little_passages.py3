# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 - Problem E. Twisty Little Passages
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45fc0
#
# Time:  O(min(K, N))
# Space: O(min(K, N))
#
# python interactive_runner.py python3 testing_tool.py 0 -- python3 twisty_little_passages.py3
#

from sys import stdout
from random import seed, shuffle

def walk():
    print("W")
    stdout.flush()
    return list(map(int, input().split()))

def teleport(i):
    print("T %s" % i)
    stdout.flush()
    return list(map(int, input().split()))

def estimate(i):
    print("E %s" % i)
    stdout.flush()

def twisty_little_passages():
    N, K = list(map(int, input().split()))
    R, P = list(map(int, input().split()))
    candidates = [i for i in range(1, N+1) if i != R]
    shuffle(candidates)
    lookup = {R}
    turn = K%2
    total = total_T = P
    cnt_T = 1
    while K and len(lookup) < N:
        if K%2 == turn:
            R, P = walk()
        else:
            while candidates[-1] in lookup:
                candidates.pop()
            R, P = teleport(candidates.pop())
            total_T += P
            cnt_T += 1
        if R not in lookup:
            lookup.add(R)
            total += P
        K -= 1
    avg = total_T/cnt_T
    estimate(int((total+avg*(N-len(lookup)))/2))

seed(0)
for case in range(int(input())):
    twisty_little_passages()
