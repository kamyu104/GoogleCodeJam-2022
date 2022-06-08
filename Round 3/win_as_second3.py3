# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 3 - Problem D. Win As Second
# https://codingcompetitions.withgoogle.com/codejam/round/00000000008779b4/0000000000b4518a
#
# Time:  precompute: O(N^L * (N * S)) = O(N^6) at worst, O(N^5) on average, L = 3 by experiments for N in [30, 40]
#        runtime:    O(N * S + M * N^2) = O(N^3 + M * N^2), S is the number of all grundy states, which is around 2500
# Space: O(S) = O(N^2)
#
# python interactive_runner.py python3 testing_tool.py3 1 -- python3 win_as_second2.py3
#
# optimized from win_as_second2.py3
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

def find_submasks(adj, mask):  # Time: O(N)
    submasks = []
    while mask:
        i = LOG2[mask&-mask]
        new_mask = bfs(adj, i, mask)
        submasks.append(mask^new_mask)
        mask = new_mask
    return submasks

def find_submasks_splitted_by_i(adj, i, new_mask):  # Time: O(1)
    j = adj[i][0] if i >= len(adj)-3 else i
    if i >= len(adj)-3 and new_mask&(1<<j):
        return [new_mask]
    submasks = []
    main_chains_mask = new_mask&((1<<(len(adj)-3))-1)
    submasks.append(main_chains_mask&((1<<j)-1))
    submasks.append(main_chains_mask^submasks[-1])
    length_1_chains_mask = new_mask^main_chains_mask
    while length_1_chains_mask:
        j = LOG2[length_1_chains_mask&-length_1_chains_mask]
        assert(len(adj[j]) == 1)
        for k in range(2):
            if submasks[k]&(1<<adj[j][0]):
                submasks[k] |= 1<<j
                break
        else:
            submasks.append(1<<j)
        length_1_chains_mask ^= 1<<j
    # since the degree of each node is at most 3, it is divided into at most 5 submasks
    assert(len(submasks) <= 5)
    return submasks

def enumerate_next_states(adj, lookup, mask):  # Time: O(N)
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
            for submask in find_submasks_splitted_by_i(adj, i, new_mask):
                ng ^= grundy(adj, submask, lookup)
            yield ng, i, new_mask
            if not neighbors_submask:
                break
            neighbors_submask = (neighbors_submask-1)&neighbors_mask
        curr ^= 1<<i

def grundy(adj, mask, lookup):  # Time: O(N)
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
def gen_edges(N):
    for a in range(1, N-4):
        for b in range(a+1, N-4):
            for c in range(b+1, N-4):
                yield [[i-1, i] for i in range(1, N-3)]+[[a, N-3]]+[[b, N-2]]+[[c, N-1]]

MIN_N = 30
EDGES = {}
for N in range(MIN_N, MAX_N+1):
    cnt = 0
    for edges in gen_edges(N):
        cnt += 1
        adj = [[] for _ in range(N)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        lookup = {}
        if not grundy(adj, (1<<N)-1, lookup):
            EDGES[N] = edges
            break
    else:
        assert(False)
    print(f"N : {N}, tried : {cnt}, states : {len(lookup)}")
print(f"EDGES = {EDGES}")
exit(0)
'''

# precomputed by the code above, it takes around 1 minutes for PyPy3 to finish
EDGES = {30: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [1, 27], [7, 28], [16, 29]], 31: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [4, 28], [14, 29], [15, 30]], 32: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [1, 29], [2, 30], [4, 31]], 33: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [1, 30], [4, 31], [10, 32]], 34: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [1, 31], [3, 32], [16, 33]], 35: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [4, 32], [8, 33], [21, 34]], 36: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [1, 33], [2, 34], [10, 35]], 37: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [1, 34], [2, 35], [31, 36]], 38: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 34], [1, 35], [2, 36], [4, 37]], 39: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 34], [34, 35], [1, 36], [4, 37], [12, 38]], 40: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13], [13, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21], [21, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28], [28, 29], [29, 30], [30, 31], [31, 32], [32, 33], [33, 34], [34, 35], [35, 36], [1, 37], [2, 38], [27, 39]]}
for case in range(int(input())):
    win_as_second()
