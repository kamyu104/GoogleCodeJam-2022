# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1C - Problem A. Letter Blocks
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afe6a1
#
# Time:  O(N * L)
# Space: O(N)
#

from collections import defaultdict, deque

def check(S, result):
    lookup = set()
    prev = None
    for i in result:
        for c in S[i]:
            if c == prev:
                continue
            if prev in lookup:
                return False
            lookup.add(prev)
            prev = c
    return prev not in lookup

def letter_blocks():
    N = int(input())
    S = list(input().split())
    left, right, both = defaultdict(set), defaultdict(set), defaultdict(set)
    for i, s in enumerate(S):
        if s[0] != s[-1]:
            left[s[0]].add(i)
            right[s[-1]].add(i)
        else:
            both[s[0]].add(i)
    result = []
    lookup = set()
    for i, s in enumerate(S):
        if i in lookup:
            continue
        lookup.add(i)
        dq = deque([i])
        for i, adj, add in ((0, right, dq.appendleft), (-1, left, dq.append)):
            while both[S[dq[i]][i]] or adj[S[dq[i]][i]]:
                j = (both[S[dq[i]][i]] if both[S[dq[i]][i]] else adj[S[dq[i]][i]]).pop()
                if j in lookup:
                    continue
                lookup.add(j)
                add(j)
        result.extend(dq)
    return "".join(map(lambda x:S[x], result)) if check(S, result) else "IMPOSSIBLE"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, letter_blocks()))
