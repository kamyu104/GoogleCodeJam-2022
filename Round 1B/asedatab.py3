# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1B - Problem C. ASeDatAb
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd29b
#
# Time:  precompute: O(L * 2^L)
#        runtime:    O(L * 2^L)
# Space: O(L * 2^L)
#
# python interactive_runner.py python3 testing_tool.py 0 -- python3 asedatab.py3
#

def ask(N):
    print(N, flush=True)
    return int(input())

def asedatab():
    for x in SEQ:
        if not ask(x):
            break

def sequence(l):
    result = ['1']
    while len(result[0]) != l:
        zero = [s+'0'*len(s) for s in result]
        copy = [s+s for s in result]
        result = []
        for x in zero:
            result.extend(copy)
            result.append(x)
        result.extend(copy)
    return result

L = 8  # should be power of 2
SEQ = sequence(L)
for case in range(int(input())):
    asedatab()
