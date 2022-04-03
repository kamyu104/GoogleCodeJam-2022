# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 - Problem D. Chain Reactions
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45ef7
#
# Time:  O(N)
# Space: O(N)
#

def chain_reaction():
    N = int(input())
    F = [0]+list(map(int, input().split()))
    P = list(map(int, input().split()))
    adj = [[] for _ in range(N+1)]
    in_degree = [0]*(N+1)
    for u, v in enumerate(P, 1):
        adj[u].append(v)
        in_degree[v] += 1
    q = [u for u in range(N+1) if not in_degree[u]]
    lookup = [[] for _ in range(N+1)]
    result = 0
    while q:
        new_q = []
        for u in q:
            for v in adj[u]:
                lookup[v].append(u)
                if len(lookup[v]) != in_degree[v]:
                    continue
                new_q.append(v)
                u = min(lookup[v], key=F.__getitem__)
                F[v] = max(F[v], F[u])
                result += sum(F[nu] for nu in lookup[v] if nu != u)
        q = new_q
    result += F[0]
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, chain_reaction()))
