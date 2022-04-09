# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1A - Problem A. Double or One Thing
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877ba5/0000000000aa8e9c
#
# Time:  O(|S|)
# Space: O(1)
#

def double_or_one_thing():
    S = input()
    result = []
    cnt = 1
    for i in range(len(S)):
        if i+1 != len(S):
            if S[i] == S[i+1]:
                cnt += 1
            else:
                if S[i] < S[i+1]:
                    result.append(S[i]*cnt)
                cnt = 1
        result.append(S[i])
    return "".join(result)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, double_or_one_thing()))
