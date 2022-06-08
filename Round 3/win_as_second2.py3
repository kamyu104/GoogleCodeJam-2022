# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 3 - Problem D. Win As Second
# https://codingcompetitions.withgoogle.com/codejam/round/00000000008779b4/0000000000b4518a
#
# Time:  precompute: O(N^L * (N^2 * S)) = O(N^7) at worst, L = 3 by experiments for N in [30, 40]
#        runtime:    O(N^2 * S + M * N^3) = O(N^4 + M * N^3), S is the number of all grundy states, which is around 2500
# Space: O(S) = O(N^2)
#
# python interactive_runner.py python3 testing_tool.py3 1 -- python3 win_as_second2.py3
#
# optimized from win_as_second.py3
#

def print_tree(edges):
    print("\n".join(map(lambda x: "%s %s" % (x[0]+1, x[1]+1), edges)), flush=True)

def print_choices(N, i, chosen_mask):
    neighbors_mask = chosen_mask^(1<<i)
    choices = [i+1]+[j+1 for j in range(N) if neighbors_mask&(1<<j)]
    print("%s\n%s" % (len(choices), " ".join(map(str, choices))), flush=True)

def mex(lookup):
    return next(i for i in range(len(lookup)+1) if i not in lookup)

def bfs(adj, i, mask):
    q = [i]
    new_mask = mask^(1<<i)
    while q:
        new_q = []
        for i in q:
            for j in adj[i]:
                if not (new_mask&(1<<j)):
                    continue
                new_mask ^= 1<<j
                new_q.append(j)
        q = new_q
    return new_mask

def find_submasks(adj, mask):
    submasks = []
    while mask:
        i = LOG2[mask&-mask]
        new_mask = bfs(adj, i, mask)
        submasks.append(mask^new_mask)
        mask = new_mask
    return submasks

def enumerate_next_states(adj, lookup, mask):
    curr = mask
    while curr:
        i = LOG2[curr&-curr]
        neighbors_mask = 0
        for j in adj[i]:
            if not (mask&(1<<j)):
                continue
            neighbors_mask |= 1<<j
        neighbors_submask = neighbors_mask
        while neighbors_submask >= 0:  # submask enumeration
            new_mask = mask^(1<<i)^neighbors_submask
            ng = 0
            for submask in find_submasks(adj, new_mask):
                ng ^= grundy(adj, submask, lookup)
            yield ng, i, new_mask
            if not neighbors_submask:
                break
            neighbors_submask = (neighbors_submask-1)&neighbors_mask
        curr ^= 1<<i

def grundy(adj, mask, lookup):
    if mask not in lookup:
        lookup[mask] = mex({ng for ng, _, _ in enumerate_next_states(adj, lookup, mask)})
    return lookup[mask]

def win_as_second():
    N = int(input())
    adj = [[] for _ in range(N)]
    for i, j in EDGES[N]:
        adj[i].append(j)
        adj[j].append(i)
    lookup = {}
    assert(grundy(adj, (1<<N)-1, lookup) == 0 and len(lookup) <= 2500)
    print_tree(EDGES[N])
    M = int(input())
    for _ in range(M):
        mask = (1<<N)-1
        while mask:
            K = int(input())
            A = list(map(lambda x: int(x)-1, input().split()))
            for i in A:
                mask ^= 1<<i
            submasks = find_submasks(adj, mask)
            g = 0
            for submask in submasks:
                g ^= grundy(adj, submask, lookup)
            assert(g != 0)
            i, submask, new_submask = next((i, submask, new_submask) for submask in submasks for ng, i, new_submask in enumerate_next_states(adj, lookup, submask) if not g^grundy(adj, submask, lookup)^ng)
            new_mask = mask^submask^new_submask
            print_choices(N, i, mask^new_mask)
            mask = new_mask

MAX_N = 40
LOG2 = {1<<i:i for i in range(MAX_N)}

'''
from random import seed, randint

def generate_edges(N):
    return [[i-1 if i < N-L else randint(0, i-1), i] for i in range(1, N)]

seed(0)
L = 3  # tuned by experiments
MIN_N = 30
EDGES = {}
for N in range(MIN_N, MAX_N+1):
    cnt = 0
    while True:
        cnt += 1
        EDGES[N] = generate_edges(N)
        adj = [[] for _ in range(N)]
        for i, j in EDGES[N]:
            adj[i].append(j)
            adj[j].append(i)
        lookup = {}
        if not grundy(adj, (1<<N)-1, lookup):
            break
    print(f"N : {N}, tried : {cnt}, states : {len(lookup)}")
print(EDGES)
exit(0)
'''

# precomputed by the code above, it takes around 6 minutes for PyPy3 to finish
EDGES = {30: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [25, 27], [26, 28], [9, 29]], 31: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [12, 28], [23, 29], [13, 30]], 32: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [26, 29], [20, 30], [2, 31]], 33: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [24, 30], [21, 31], [2, 32]], 34: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [11, 31], [16, 32], [8, 33]], 35: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [0, 32], [30, 33], [33, 34]], 36: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [27, 33], [29, 34], [8, 35]], 37: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [7, 34], [16, 35], [29, 36]], 38: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 34], [6, 35], [4, 36], [13, 37]], 39: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 34], [34, 35], [12, 36], [4, 37], [12, 38]], 40: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 34], [34, 35], [35, 36], [33, 37], [7, 38], [26, 39]]}
for case in range(int(input())):
    win_as_second()
