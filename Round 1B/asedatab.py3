# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 1B - Problem C. ASeDatAb
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd29b
#
# Time:  precompute: O(states) * O(candidates) * O(L) * O(max_state_len) = O(1607200)
#        runtime:    O((max_state_len + L) * max_depth) = O((10 + 8) * 12) = O(216)
# Space: O(states) * O(candidates) * O(L) * O(max_state_len) = O(1607200)
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
    state = None
    while cnt:  # repeat at most O(max_detph) = O(12) times
        state = ADJ[state, CHOICES[state]][cnt] if state else INIT_STATES[cnt]  # Time: O(max_state_len) = O(10)
        cnt = save("{0:08b}".format(CHOICES[state]))  # Time: O(L)

def enumerate_rotation(x):
    return ((x>>r) | (x&((1<<r)-1))<<(L-r) for r in range(L))

def norm(x):
    return min(enumerate_rotation(x))

def group_by_bitcount(a):
    bcnt_to_state = defaultdict(set)
    for x in a:
        bcnt_to_state[bin(x).count('1')].add(norm(x))
    for cnt, state in bcnt_to_state.items():
        bcnt_to_state[cnt] = tuple(sorted(state))
    return bcnt_to_state

def bfs(bcnt_to_state):  # enumerate all possible states
    adj = {}
    prevs = defaultdict(list)
    candidates = list(chain.from_iterable(bcnt_to_state.values()))  # Space: O(35)
    q = bcnt_to_state.values()
    for x in q:
        prevs[x]
    while q:
        new_q = []
        for state in q:
            for v in candidates:
                adj[state, v] = group_by_bitcount((x^w for w in enumerate_rotation(v) for x in state))  # Time / Space in total: O(states) * O(candidates) * O(L) * O(max_state_len) = O(574) * O(35) * O(8) * O(10) = O(1607200)
                for new_state in adj[state, v].values():
                    if new_state not in prevs:
                        new_q.append(new_state)
                    prevs[new_state].append((state, v))  # Space: O(states) * O(candidates) * O(max_state_len) = O(574) * O(35) * O(10) = O(200900)
        q = new_q
    return adj, prevs

def topological_sort(adj, prevs):  # find choices to reach zero state
    in_degree = defaultdict(int)  # Space: O(states) * O(candidates) * O(max_state_len) = O(574) * O(35) * O(10) = O(200900)
    choices = {(0,):-1}  # Space: O(states) * O(max_state_len) = O(574)* O(10) = O(5740)
    q = [(0,)]
    while q:
        new_q = []
        for state in q:
            for prev_state, v in prevs[state]:
                in_degree[prev_state, v] += 1
                if in_degree[prev_state, v] != len(adj[prev_state, v]) or prev_state in choices:
                    continue
                choices[prev_state] = v
                new_q.append(prev_state)
        q = new_q
    return choices

def precompute():
    bcnt_to_state = group_by_bitcount(range(1, 1<<L))
    adj, prevs = bfs(bcnt_to_state)
    choices = topological_sort(adj, prevs)
    assert(all(x in choices for x in bcnt_to_state.values()))
    return bcnt_to_state, adj, choices

L = 8  # should be a power of 2
INIT_STATES, ADJ, CHOICES = precompute()
for case in range(int(input())):
    asedatab()
