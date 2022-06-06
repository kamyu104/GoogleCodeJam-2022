# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 3 - Problem C. Mascot Maze
# https://codingcompetitions.withgoogle.com/codejam/round/00000000008779b4/0000000000b44a4f
#
# Time:  O(N), pass in PyPy3 but Python3
# Space: O(N)
#

from itertools import chain

def mascot_maze():
    N = int(input())
    L = list(map(lambda x: int(x)-1, input().split()))
    R = list(map(lambda x: int(x)-1, input().split()))
    adj = [[] for _ in range(N)]
    adj2 = [[] for _ in range(N)]
    for u, (l, r) in enumerate(zip(L, R)):
        neis = {l, L[l], R[l], r, L[r], R[r]}
        if u in neis:
            return "IMPOSSIBLE"
        adj[u] = list(neis)
        for v in adj[u]:
            adj2[v].append(u)
    order = []
    degree = [len(adj[u])+len(adj2[u]) for u in range(N)]
    q = [u for u in range(N) if degree[u] < len(MOSCOTS)]
    lookup = [degree[u] < len(MOSCOTS) for u in range(N)]
    while q:
        new_q = []
        for u in q:
            order.append(u)
            for v in chain(adj[u], adj2[u]):
                degree[v] -= 1
                if degree[v] >= len(MOSCOTS) or lookup[v]:
                    continue
                lookup[v] = True
                new_q.append(v)
        q = new_q
    result = [None]*N
    for u in reversed(order):
        used = set(result[v] for v in chain(adj[u], adj2[u]) if result[v])
        result[u] = next(x for x in MOSCOTS if x not in used)
    return "".join(result)

MOSCOTS = "ACDEHIJKMORST"
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, mascot_maze()))
