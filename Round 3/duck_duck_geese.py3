# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 3 - Problem B. Duck, Duck, Geese
# https://codingcompetitions.withgoogle.com/codejam/round/00000000008779b4/0000000000b45244
#
# Time:  O(NlogN), TLE in both Python3 / PyPy3 for test case 2
# Space: O(N)
#

class SegmentTree(object):  # 0-based index
    def __init__(self, N,
                 build_fn=lambda _: 0,
                 query_fn=lambda x, y: y if x is None else max(x, y),
                 update_fn=lambda x, y: y if x is None else x+y):
        self.base = N
        self.H = (N-1).bit_length()
        self.query_fn = query_fn
        self.update_fn = update_fn
        self.tree = [None]*(2*N)
        self.lazy = [None]*N
        for i in range(self.base, self.base+N):
            self.tree[i] = build_fn(i-self.base)
        for i in reversed(range(1, self.base)):
            self.tree[i] = query_fn(self.tree[2*i], self.tree[2*i+1])

    def __apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.base:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def update(self, L, R, h):  # Time: O(logN), Space: O(N)
        def pull(x):
            while x > 1:
                x //= 2
                self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2+1])
                if self.lazy[x] is not None:
                    self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

        if L > R:
            return
        L += self.base
        R += self.base
        L0, R0 = L, R
        while L <= R:
            if L & 1:  # is right child
                self.__apply(L, h)
                L += 1
            if R & 1 == 0:  # is left child
                self.__apply(R, h)
                R -= 1
            L //= 2
            R //= 2
        pull(L0)
        pull(R0)

    def query(self, L, R):  # Time: O(logN), Space: O(N)
        def push(x):
            n = 2**self.H
            while n != 1:
                y = x // n
                if self.lazy[y] is not None:
                    self.__apply(y*2, self.lazy[y])
                    self.__apply(y*2 + 1, self.lazy[y])
                    self.lazy[y] = None
                n //= 2

        result = None
        if L > R:
            return result

        L += self.base
        R += self.base
        push(L)
        push(R)
        while L <= R:
            if L & 1:  # is right child
                result = self.query_fn(result, self.tree[L])
                L += 1
            if R & 1 == 0:  # is left child
                result = self.query_fn(result, self.tree[R])
                R -= 1
            L //= 2
            R //= 2
        return result

def duck_duck_geese():
    def build(N):
        return [0, 1]

    def query(x, y):
        if x is None:
            return y
        if x[0] != y[0]:
            return max(x, y)
        return [x[0], x[1]+y[1]]

    def update(x, y):
        if x is None:
            return y
        return [x[0]+y[0], x[1]]

    def add(idx, i, a, b, diff):
        st.update((idx[i-1]+1 if i-1 >= 0 else 0), (idx[i]-1 if i < len(idx) else 2*N-1), diff)
        if i+a-1 < len(idx):
            st.update(idx[i+a-1], (idx[i+b]-1 if i+b < len(idx) else 2*N-1), diff)

    N, C = map(int, input().split())
    A, B = [0]*N, [0]*N
    for i in range(C):
        A[i], B[i] = map(int, input().split())
        A[i] = max(A[i], 1)
    P = list(map(lambda x: int(x)-1, input().split()))
    idx = [[] for _ in range(C)]
    for i in range(2*N):
        idx[P[i%N]].append(i)
    st = SegmentTree(2*N, build_fn=build, query_fn=query, update_fn=update)
    curr = [0]*C
    for c in range(C):
        add(idx[c], curr[c], A[c], B[c], [+1, None])
    result = 0
    for i, c in enumerate(P):
        mx, cnt = st.query(i+1, i+N-2)
        if mx == C:
            result += cnt
        add(idx[c], curr[c], A[c], B[c], [-1, None])
        curr[c] += 1
        add(idx[c], curr[c], A[c], B[c], [+1, None])
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, duck_duck_geese()))
