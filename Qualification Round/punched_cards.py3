# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 - Problem A. Punched Cards
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b
#
# Time:  O(R * C)
# Space: O(1)
#

def punched_cards():
    R, C = list(map(int, input().split()))
    result = [[ASCII[1][1] if i < 2 and j < 2 else ASCII[i%2][j%2]for j in range(2*C+1)] for i in range(2*R+1)]
    return "\n%s" % "\n".join(map(lambda x: "".join(x), result))

ASCII = ["+-", "|."]
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, punched_cards()))
