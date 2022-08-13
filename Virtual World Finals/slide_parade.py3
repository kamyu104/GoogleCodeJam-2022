# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Virtual World Finals - Problem C. Slide Parade
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087762e/0000000000b9cb13
#
# Time:  O(B * S + S^2), pass in PyPy3 but Python3
# Space: O(B * S)
#

def bfs(adj):
    lookup = [False]*len(adj)
    q = [0]
    lookup[0] = True
    while q:
        new_q = []
        for u in q:
            for v in adj[u]:
                if lookup[v]:
                    continue
                lookup[v] = True
                new_q.append(v)
        q = new_q
    return sum(lookup)

# Hungarian algorithm
def augment(adj, u, ignore, lookup, match):
    for v in adj[u]:
        if v == ignore or v in lookup:
            continue
        lookup.add(v)
        if v not in match or augment(adj, match[v], ignore, lookup, match):
            match[v] = u  # greedily match
            return True
    return False

def find_alternating_matching(adj, u, v, match):  # Time: O(S)
    if match[v] != u:
        del match[next(x for x, y in match.items() if y == u)]
        if not augment(adj, match[v], v, set(), match):
            return False
        match[v] = u
    return True

# Hierholzer algorithm
def Hierholzer(adj):
    result = []
    stk = [0]
    while stk:
        while adj[stk[-1]]:
            stk.append(adj[stk[-1]].pop())
        result.append(stk.pop())
    result.reverse()
    return result

def slide_parade():
    B, S = list(map(int, input().split()))
    adj = [[] for _ in range(B)]
    for _ in range(S):
        U, V = list(map(int, input().split()))
        U -= 1
        V -= 1
        adj[U].append(V)
    if bfs(adj) != B:
        return "IMPOSSIBLE"
    match = {}
    for u in range(B):  # Time: O(B * S)
        augment(adj, u, -1, set(), match)
    if len(match) != B:
        return "IMPOSSIBLE"
    adj2 = [[] for _ in range(B)]
    for u in range(B):  # Time: O(S^2 + S * B), Space: O(S * B)
        for v in adj[u]:
            if not find_alternating_matching(adj, u, v, match):
                return "IMPOSSIBLE"
            for u in range(B):
                adj2[match[u]].append(u)
    result = Hierholzer(adj2)  # Time: O(B * S)
    return "%s\n%s" % (len(result), " ".join(map(lambda x: str(x+1), result)))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, slide_parade()))
