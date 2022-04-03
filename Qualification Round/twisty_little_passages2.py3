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

def walk():
    print("W", flush=True)
    return list(map(int, input().split()))

def teleport(i):
    print("T %s" % i, flush=True)
    return list(map(int, input().split()))

def estimate(i):
    print("E %s" % i, flush=True)

def twisty_little_passages():
    N, K = list(map(int, input().split()))
    R, P = list(map(int, input().split()))
    candidates = {i for i in range(1, N+1) if i != R}
    degree = P
    weight = 1
    for i in range(K):
        if not candidates:
            break
        if i%2 == 0:
            prev = P
            R, P = walk()
            degree += P*(prev/P)
            weight += prev/P
        else:
            R, P = teleport(next(iter(candidates)))
            degree += P*1
            weight += 1
        if R in candidates:
            candidates.remove(R)
    avg = degree/weight
    estimate(int((avg*N)/2))

for case in range(int(input())):
    twisty_little_passages()
