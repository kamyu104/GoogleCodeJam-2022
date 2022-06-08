# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 3 - Problem D. Win As Second
# https://codingcompetitions.withgoogle.com/codejam/round/00000000008779b4/0000000000b4518a
#
# Time:  O(N^L * (N * S)) + O(N * S + M * N^2) = O(N^6) at worst, O(N^5) on average, L = 3 by experiments for N in [30, 40]
# Space: O(S) = O(N^2), S is the number of all grundy states, which is around 2500
#
# python interactive_runner.py python3 testing_tool.py3 1 -- python3 win_as_second2.py3
#
# optimized from win_as_second3.py3, no need to precompute
# pass in PyPy3 but Python3
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
    j = i if i < len(adj)-3 else adj[i][0] if not (new_mask&(1<<adj[i][0])) else len(adj)-3
    submasks = [0]*2
    main_chains_mask = new_mask&((1<<(len(adj)-3))-1)
    submasks[0] = main_chains_mask&((1<<j)-1)
    submasks[1] = main_chains_mask^submasks[0]
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
    # since the degree of each node we construct is at most 3, it is divided into at most 5 submasks
    assert(len(adj[i]) <= 3 and len(submasks) <= 5)
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

def gen_edges(N):
    # tree class:
    #   o   o  o     3 chains of length 1
    # ooooooooooooo  1 main chain
    #
    for a in range(1, N-4):
        for b in range(a+1, N-4):
            for c in range(b+1, N-4):
                edges = [[i-1, i] for i in range(1, N)]
                edges[-3][0], edges[-2][0], edges[-1][0] = a, b, c
                yield edges

def find_edges(N):
    cnt = 0
    for edges in gen_edges(N):
        cnt += 1
        adj = [[] for _ in range(N)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        lookup = {}
        if not grundy(adj, (1<<N)-1, lookup):
            break
    else:
        assert(False)
    return edges, lookup

def win_as_second():
    N = int(input())
    edges, lookup = find_edges(N)
    adj = [[] for _ in range(N)]
    for i, j in edges:
        adj[i].append(j)
        adj[j].append(i)
    assert(grundy(adj, (1<<N)-1, lookup) == 0 and len(lookup) <= 2500)
    print_tree(edges)
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
for case in range(int(input())):
    win_as_second()
