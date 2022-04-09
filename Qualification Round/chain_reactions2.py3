# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Qualification Round - Problem D. Chain Reactions
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
    for u, v in enumerate(P, 1):
        adj[v].append(u)
    result = 0
    for v in reversed(range(N)):
        if not adj[v]:
            continue
        u = min(adj[v], key=F.__getitem__)
        F[v] = max(F[v], F[u])
        result += sum(F[nu] for nu in adj[v] if nu != u)
    result += F[0]
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, chain_reaction()))
