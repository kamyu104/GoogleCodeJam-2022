# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Virtual World Finals - Problem A. Wonderland Chase
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087762e/0000000000b9c499
#
# Time:  O(J + C)
# Space: O(J + C)
#

def bfs1(adj, degree):
    is_leaf = [False]*len(adj)
    q = [u for u in range(len(adj)) if degree[u] <= 1]
    for u in q:
        is_leaf[u] = True
    while q:
        new_q = []
        for u in q:
            for v in adj[u]:
                degree[v] -= 1
                if degree[v] > 1 or is_leaf[v]:
                    continue
                is_leaf[v] = True
                new_q.append(v)
        q = new_q
    return is_leaf

def bfs2(adj, u):
    dist = [INF]*len(adj)
    q = [u]
    dist[u] = 0
    while q:
        new_q = []
        for u in q:
            for v in adj[u]:
                if dist[v] != INF:
                    continue
                dist[v] = dist[u]+1
                new_q.append(v)
        q = new_q
    return dist

def wonderland_chase():
    J, C, A, Q = list(map(int, input().split()))
    A -= 1
    Q -= 1
    adj = [[] for _ in range(J)]
    degree = [0]*J
    for _ in range(C):
        U, V = list(map(int, input().split()))
        adj[U-1].append(V-1)
        adj[V-1].append(U-1)
        degree[U-1] += 1
        degree[V-1] += 1
    is_leaf = bfs1(adj, degree)
    dist_A = bfs2(adj, A)
    dist_Q = bfs2(adj, Q)
    if dist_Q[A] == INF or any(not is_leaf[u] and dist_A[u] < dist_Q[u] for u in range(J)):
        return "SAFE"
    return 2*max((dist_Q[u] for u in range(J) if dist_A[u] < dist_Q[u]))

INF = float("inf")
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, wonderland_chase()))
