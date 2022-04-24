# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1B - Problem C. ASeDatAb
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd29b
#
# Time:  O(N)
# Space: O(1)
#
# python interactive_runner.py python3 testing_tool.py 0 -- python3 asedatab.py3
#

def ask(N):
    print(N, flush=True)
    return int(input())

def solution():
    for x in SEQ:
        if not ask(x):
            break

def P(k):
    result = ['1']
    for _ in range(k):
        zero = [s+'0'*len(s) for s in result]
        copy = [s+s for s in result]
        result = copy[:]
        for x in zero:
            result.append(x)
            result.extend(copy)
    return result

SEQ = P(3)
for case in range(int(input())):
    solution()
