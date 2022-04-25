# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1B - Problem C. ASeDatAb
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd29b
#
# Time:  precompute: O(L * 2^L)
#        runtime:    O(L * 2^L)
# Space: O(L * 2^L)
#
# python interactive_runner.py python3 testing_tool.py 0 -- python3 asedatab.py3
#

from collections import defaultdict
from itertools import chain

def save(N):
    print(N, flush=True)
    return int(input())

def asedatab():
    cnt = save("{0:08b}".format((1<<L)-1))
    if not cnt:
        return
    states = BCNTS
    while True:
        state = states[cnt]
        v = NXTS[state]
        cnt = save("{0:08b}".format(v))
        if not cnt:
            break
        states = ADJ[state, v]

def rotates(x):
    return ((x>>r) | (x&((1<<r)-1))<<(L-r) for r in range(L))

def norm(x):
    return min(rotates(x))

def bitcount(a):
    bcnts = defaultdict(set)
    for x in a:
        bcnts[bin(x).count('1')].add(norm(x))
    for cnt, state in bcnts.items():
        bcnts[cnt] = tuple(sorted(state))
    return bcnts

def bfs(bcnts):
    adj = {}
    prevs = defaultdict(list)
    q = bcnts.values()
    lookup = set(q)
    while q:
        new_q = []
        for state in q:
            for v in chain.from_iterable(bcnts.values()):
                adj[state, v] = bitcount((x^w for w in rotates(v) for x in state))
                for new_state in adj[state, v].values():
                    prevs[new_state].append((state, v))
                    if new_state in lookup:
                        continue
                    lookup.add(new_state)
                    new_q.append(new_state)
        q = new_q
    return adj, prevs

def topological_sort(adj, prevs):
    in_degree = defaultdict(int)
    nxts = {}
    q = [(0,)]
    lookup = set(q)
    while q:
        new_q = []
        for state in q:
            for prev_state, v in prevs[state]:
                in_degree[prev_state, v] += 1
                if in_degree[prev_state, v] != len(adj[prev_state, v]) or prev_state in lookup:
                    continue
                lookup.add(prev_state)
                new_q.append(prev_state)
                nxts[prev_state] = v
        q = new_q
    return nxts

def precompute():
    bcnts = bitcount(range(1, 1<<L))
    adj, prevs = bfs(bcnts)
    nxts = topological_sort(adj, prevs)
    return bcnts, adj, nxts

L = 8  # should be a power of 2
BCNTS, ADJ, NXTS = precompute()
for case in range(int(input())):
    asedatab()
