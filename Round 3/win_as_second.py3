# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 3 - Problem D. Win As Second
# https://codingcompetitions.withgoogle.com/codejam/round/00000000008779b4/0000000000b4518a
#
# Time:  precompute: O(N * S), S is around 250,000
# #      runtime:    O(N^2)
# Space: O(S)
#
# python interactive_runner.py python3 testing_tool.py3 1 -- python3 win_as_second.py3
#

from sys import stdout

def print_tree(edges):
    for i, j in edges:
        print(i+1, j+1)
    stdout.flush()

def print_choices(N, i, chosen_mask):
    neighbors_mask = chosen_mask^(1<<i)
    choices = [i+1]+[j+1 for j in range(N) if neighbors_mask&(1<<j)]
    print("%s\n%s" % (len(choices), " ".join(map(str, choices))), flush=True)

def mex(lookup):
    return next(i for i in range(len(lookup)+1) if i not in lookup)

def find_submasks(adj, mask):
    submasks = []
    total_submasks = 0
    for i in range(len(adj)):
        if not (mask&(1<<i)) or total_submasks&(1<<i):
            continue
        q = [i]
        submask = 1<<i
        while q:
            new_q = []
            for i in q:
                for j in adj[i]:
                    if not (mask&(1<<j)) or (submask&(1<<j)):
                        continue
                    submask |= 1<<j
                    new_q.append(j)
            q = new_q
        total_submasks |= submask
        submasks.append(submask)
    return submasks

def enumerate_next_states(adj, lookup, mask):
    for i in range(len(adj)):
        if not (mask&(1<<i)):
            continue
        adj_i = [j for j in adj[i] if mask&(1<<j)]
        for submask in range(1<<len(adj_i)):
            new_mask = mask^(1<<i)
            for j in range(len(adj_i)):
                if not (submask&(1<<j)):
                    continue
                new_mask ^= 1<<adj_i[j]
            yield grundy(adj, new_mask, lookup), i, new_mask

def grundy(adj, mask, lookup):
    if mask not in lookup:
        submasks = find_submasks(adj, mask)
        if len(submasks) == 1:
            lookup[mask] = mex({g for g, _, _ in enumerate_next_states(adj, lookup, mask)})
        else:
            lookup[mask] = 0
            for submask in submasks:
                lookup[mask] ^= grundy(adj, submask, lookup)
    return lookup[mask]

def win_as_second():
    N = int(input())
    adj = [[] for _ in range(N)]
    for i, j in EDGES[N]:
        adj[i].append(j)
        adj[j].append(i)
    lookup = {}
    assert(grundy(adj, (1<<N)-1, lookup) == 0)
    print_tree(EDGES[N])
    for _ in range(int(input())):
        mask = (1<<N)-1
        while mask:
            K = int(input())
            A = list(map(lambda x: int(x)-1, input().split()))
            for i in A:
                mask ^= 1<<i
            assert(grundy(adj, mask, lookup) != 0)
            i, new_mask = next((i, new_mask) for g, i, new_mask in enumerate_next_states(adj, lookup, mask) if not g)
            print_choices(N, i, mask^new_mask)
            mask = new_mask

'''
from random import seed, randint

def edges(N):
    return [[i-1 if i < N-5 else randint(0, i-1), i] for i in range(1, N)]

seed(0)
MIN_N = 30
MAX_N = 40
EDGES = {}
for N in range(MIN_N, MAX_N+1):
    while True:
        adj = [[] for _ in range(N)]
        EDGES[N] = edges(N)
        for i, j in EDGES[N]:
            adj[i].append(j)
            adj[j].append(i)
        lookup = {}
        if not grundy(adj, (1<<N)-1, lookup):
            break
print(EDGES)
exit(0)
'''

# precomputed by the code above, it takes around 6 minutes for PyPy3 to complete
EDGES = {30: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [6, 25], [16, 26], [4, 27], [9, 28], [4, 29]], 31: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [6, 26], [5, 27], [14, 28], [11, 29], [25, 30]], 32: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [5, 27], [11, 28], [1, 29], [23, 30], [20, 31]], 33: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [3, 28], [10, 29], [23, 30], [6, 31], [19, 32]], 34: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [22, 29], [26, 30], [18, 31], [1, 32], [24, 33]], 35: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [17, 30], [11, 31], [2, 32], [21, 33], [14, 34]], 36: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [20, 31], [11, 32], [16, 33], [23, 34], [33, 35]], 37: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [10, 32], [17, 33], [22, 34], [7, 35], [7, 36]], 38: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [0, 33], [12, 34], [19, 35], [11, 36], [10, 37]], 39: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [3, 34], [1, 35], [21, 36], [27, 37], [30, 38]], 40: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 34], [5, 35], [16, 36], [34, 37], [22, 38], [9, 39]]}
for case in range(int(input())):
    win_as_second()
