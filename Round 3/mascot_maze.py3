# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 3 - Problem C. Mascot Maze
# https://codingcompetitions.withgoogle.com/codejam/round/00000000008779b4/0000000000b44a4f
#
# Time:  O(N)
# Space: O(N)
#

def mascot_maze():
    N = int(input())
    L = list(map(lambda x: int(x)-1, input().split()))
    R = list(map(lambda x: int(x)-1, input().split()))
    adj = [[] for _ in range(N)]
    for u, (l, r) in enumerate(zip(L, R)):
        vs = {l, L[l], R[l], r, L[r], R[r]}
        if u in vs:
            return "IMPOSSIBLE"
        for v in vs:
            adj[u].append(v)
            adj[v].append(u)
    order = []
    degree = [len(adj[u]) for u in range(N)]
    q = [u for u in range(N) if degree[u] < len(MASCOTS)]
    while q:
        new_q = []
        for u in q:
            order.append(u)
            for v in adj[u]:
                degree[v] -= 1
                if degree[v] != len(MASCOTS)-1:
                    continue
                new_q.append(v)
        q = new_q
    result = [0]*N
    for u in reversed(order):
        used = {result[v] for v in adj[u] if result[v]}
        result[u] = next(x for x in MASCOTS if x not in used)
    return "".join(result)

MASCOTS = "ACDEHIJKMORST"
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, mascot_maze()))
