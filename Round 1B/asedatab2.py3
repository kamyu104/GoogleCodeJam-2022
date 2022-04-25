# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1B - Problem C. ASeDatAb
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd29b
#
# Time:  precompute: O(L * 2^L)
#        runtime:    O(L * 2^L)
# Space: O(L * 2^L)
#
# python interactive_runner.py python3 testing_tool.py 0 -- python3 asedatab2.py3
#

def save(N):
    print(N, flush=True)
    return int(input())

def asedatab():
    for x in SEQ:
        if not save("{0:08b}".format(x)):
            break

def sequence(L):
    result = [1]
    l = 1
    while l != L:
        new_result = [(x<<l)|x for x in result]
        for x in result:
            new_result.append(x)
            new_result.extend((x<<l)|x for x in result)
        result = new_result
        l <<= 1
    return result

L = 8  # should be a power of 2
SEQ = sequence(L)
for case in range(int(input())):
    asedatab()
