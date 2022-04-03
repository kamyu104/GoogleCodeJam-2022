# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 - Problem E. Twisty Little Passages
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45fc0
#
# Time:  O(min(K, N))
# Space: O(min(K, N))
#
# python interactive_runner.py python3 testing_tool.py 0 -- python3 twisty_little_passages2.py3
#

from sys import stdout

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
    candidates = set(i for i in range(1, N+1) if i != R)
    turn = K%2
    degree = P
    weight = 1
    while K and candidates:
        if K%2 == turn:
            prev = P
            R, P = walk()
            degree += P*(prev/P)
            weight += prev/P
            if R in candidates:
                candidates.remove(R)
        else:
            R, P = teleport(candidates.pop())
            degree += P*1
            weight += 1
        K -= 1
    avg = degree/weight
    estimate(int((avg*N)/2))

for case in range(int(input())):
    twisty_little_passages()
