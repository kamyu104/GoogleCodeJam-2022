# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 2 - Problem C. Saving the Jelly
# https://codingcompetitions.withgoogle.com/codejam/round/00000000008778ec/0000000000b158f8
#
# Time:  O(N^2 * sqrt(N)), pass in PyPy3 but Python3
# Space: O(N)
#

from functools import partial
from collections import defaultdict

# Time:  O(E * sqrt(V))
# Space: O(V)
# Source code from http://code.activestate.com/recipes/123641-hopcroft-karp-bipartite-matching/
# Hopcroft-Karp bipartite max-cardinality matching and max independent set
# David Eppstein, UC Irvine, 27 Apr 2002
def bipartiteMatch(graph):
    '''Find maximum cardinality matching of a bipartite graph (U,V,E).
    The input format is a dictionary mapping members of U to a list
    of their neighbors in V.  The output is a triple (M,A,B) where M is a
    dictionary mapping members of V to their matches in U, A is the part
    of the maximum independent set in U, and B is the part of the MIS in V.
    The same object may occur in both U and V, and is treated as two
    distinct vertices if this happens.'''
    
    # initialize greedy matching (redundant, but faster than full search)
    matching = {}
    for u in graph:
        for v in graph[u]:
            if v not in matching:
                matching[v] = u
                break
    
    while 1:
        # structure residual graph into layers
        # pred[u] gives the neighbor in the previous layer for u in U
        # preds[v] gives a list of neighbors in the previous layer for v in V
        # unmatched gives a list of unmatched vertices in final layer of V,
        # and is also used as a flag value for pred[u] when u is in the first layer
        preds = {}
        unmatched = []
        pred = dict([(u,unmatched) for u in graph])
        for v in matching:
            del pred[matching[v]]
        layer = list(pred)
        
        # repeatedly extend layering structure by another pair of layers
        while layer and not unmatched:
            newLayer = {}
            for u in layer:
                for v in graph[u]:
                    if v not in preds:
                        newLayer.setdefault(v,[]).append(u)
            layer = []
            for v in newLayer:
                preds[v] = newLayer[v]
                if v in matching:
                    layer.append(matching[v])
                    pred[matching[v]] = v
                else:
                    unmatched.append(v)
        
        # did we finish layering without finding any alternating paths?
        if not unmatched:
            unlayered = {}
            for u in graph:
                for v in graph[u]:
                    if v not in preds:
                        unlayered[v] = None
            return (matching,list(pred),list(unlayered))

        # recursively search backward through layers to find alternating paths
        # recursion returns true if found path, false otherwise
        def recurse(v):
            if v in preds:
                L = preds[v]
                del preds[v]
                for u in L:
                    if u in pred:
                        pu = pred[u]
                        del pred[u]
                        if pu is unmatched or recurse(pu):
                            matching[v] = u
                            return 1
            return 0
        
        def recurse_iter(v):
            def divide(v):
                if v not in preds:
                    return
                L = preds[v]
                del preds[v]
                for u in L :
                    if u in pred and pred[u] is unmatched:  # early return
                        del pred[u]
                        matching[v] = u
                        ret[0] = True
                        return
                stk.append(partial(conquer, v, iter(L)))

            def conquer(v, it):
                for u in it:
                    if u not in pred:
                        continue
                    pu = pred[u]
                    del pred[u]
                    stk.append(partial(postprocess, v, u, it))
                    stk.append(partial(divide, pu))
                    return

            def postprocess(v, u, it):
                if not ret[0]:
                    stk.append(partial(conquer, v, it))
                    return
                matching[v] = u

            ret, stk = [False], []
            stk.append(partial(divide, v))
            while stk:
                stk.pop()()
            return ret[0]

        for v in unmatched: recurse_iter(v)

def dist(x, y):
    return (x[0]-y[0])**2 + (x[1]-y[1])**2

def add_result(u_v, M, result):
    for v, u in M.items():
        while u_v[u][-1] not in M:
            u_v[u].pop()
        if u_v[u][-1] == v:
            result.append((u+1, v+1))
            del M[v]
            return True
    return False

def alternate_path(u_v, M):
    u = next((u for u in M.values()))
    path = [u]
    lookup = set(path)
    while True:
        while u_v[u][-1] not in M:
            u_v[u].pop()
        v = u_v[u][-1]
        u = M[v]
        if u in lookup:
            break
        path.append(u)
        lookup.add(u)
    while True:
        nu = path.pop()
        M[u_v[nu][-1]] = nu
        if nu == u:
            break

def saving_the_jelly():
    N = int(input())
    children = [list(map(int, input().split())) for _ in range(N)]
    candies = [list(map(int, input().split())) for _ in range(N+1)]
    u_v = defaultdict(list)
    for u, child in enumerate(children):
        d = dist(child, candies[0])
        for v in range(1, N+1):
            if dist(child, candies[v]) <= d:
                u_v[u].append(v)
        u_v[u].sort(key=lambda x: dist(child, candies[x]), reverse=True)
    M = bipartiteMatch(u_v)[0]
    if len(M) < N:
        return "IMPOSSIBLE"
    result = []
    while len(result) < N:
        if not add_result(u_v, M, result):
            alternate_path(u_v, M)
            add_result(u_v, M, result)
    return "POSSIBLE\n%s" % ("\n".join(map(lambda x: "%s %s"%(x[0], x[1]), result)))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, saving_the_jelly()))
