# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1B - Problem C. ASeDatAb
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd29b
#
# Time:  O(L * 2^L)
# Space: O(L)
#
# python interactive_runner.py python3 testing_tool.py 0 -- python3 asedatab3.py3
#

def sequence(L):
    if L == 1:
        yield 1
        return
    L //= 2
    for x in sequence(L):
        yield (x<<L)|x
    for x in sequence(L):
        yield x
        for x in sequence(L):
            yield (x<<L)|x

def save(N):
    print(N, flush=True)
    return int(input())

def asedatab():
    for x in sequence(L):
        if not save("{0:08b}".format(x)):
            break

L = 8  # should be a power of 2
for case in range(int(input())):
    asedatab()
