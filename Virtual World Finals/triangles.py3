# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Virtual World Finals - Problem E. Triangles
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087762e/0000000000b9c555
#
# Time:  O(N^2), pass in PyPy3 but Python3
# Space: O(N)
#

def vector(a, b):
    return [a[0]-b[0], a[1]-b[1]]

def inner_product(a, b):
    return a[0] * b[0] + a[1] * b[1]

def outer_product(a, b):
    return a[0] * b[1] - a[1] * b[0]

def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def cross(A, B, C, D):
    return ccw(A,C,D) * ccw(B,C,D) < 0 and ccw(A,B,C) * ccw(A,B,D) < 0

def insort(P, sorted_remain, x):
    sorted_remain.insert(next((i for i, y in enumerate(sorted_remain) if P[y] > P[x]), len(sorted_remain)), x)

def remove_unused(P, sorted_remain, C, a, v, result):
    cnt = sum(outer_product(v, vector(P[a], p)) == 0 for p in P)
    remove_cnt = max(cnt-2*(len(P)-cnt), 0)
    while len(C) < remove_cnt:
        for i in result.pop():
            insort(P, sorted_remain, i)
            if outer_product(v, vector(P[a], P[i])) == 0:
                C.add(i)
    for _ in range(remove_cnt):
        sorted_remain.remove(C.pop())

def find_nearest_point(P, sorted_remain, x, y):
    d1, z1, v1 = float("inf"), -1, []
    d2, z2, v2 = float("inf"), -1, []
    u = vector(P[y], P[x])
    for c in sorted_remain:
        v = vector(P[y], P[c])
        side = outer_product(u, v)
        if side == 0:
            continue
        d = inner_product(v, v)
        if side > 0:
            if z1 != -1 and outer_product(v1, v) == 0:
                if d < d1:
                    d1, z1, v1 = d, c, v
            elif z1 == -1 or outer_product(v1, v) < 0:
                d1, z1, v1 = d, c, v
        else:
            if z2 != -1 and outer_product(v2, v) == 0:
                if d < d2:
                    d2, z2, v2 = d, c, v
            elif z2 == -1 or outer_product(v2, v) > 0:
                d2, z2, v2 = d, c, v
    return z1 if z1 != -1 else z2

def make_triangle_from_maximal_points(P, sorted_remain, result):
    x, y = sorted_remain[-1], sorted_remain[-2]
    z = find_nearest_point(P, sorted_remain, x, y)
    if z == -1:
        return False
    result.append((x, y, z))
    for i in result[-1]:
        sorted_remain.remove(i)
    return True

def make_triangles_from_max_colinear(P, sorted_remain, C, result):
    other, colinear = [], []
    for x in sorted_remain:
        if x not in C:
            other.append(x)
        else:
            colinear.append(x)
    assert(len(colinear) <= 2*len(other))
    for _ in range(len(colinear)//2):
        x, y = colinear.pop(), colinear.pop()
        z = find_nearest_point(P, other, x, y)
        other.remove(z)
        result.append((x, y, z))
        for i in result[-1]:
            sorted_remain.remove(i)

def make_triangles_for_special_case(P, sorted_remain, result):
    i = 0
    for j in range(i+1, len(sorted_remain)):
        for k in range(j+1, len(sorted_remain)):
            x, y, z = sorted_remain[i], sorted_remain[j], sorted_remain[k]
            if ccw(P[x], P[y], P[z]) == 0:
                continue
            a, b, c = [o for o in sorted_remain if o not in [x, y, z]]
            if (ccw(P[a], P[b], P[c]) == 0 or
                any(cross(A, B, C, D) for A, B in ((P[x], P[y]), (P[y], P[z]), (P[z], P[x]))
                                      for C, D in ((P[a], P[b]), (P[b], P[c]), (P[c], P[a])))):
                continue
            for A, B, C in ((x, y, z), (a, b, c)):
                result.append((A, B, C))
                for i in result[-1]:
                    sorted_remain.remove(i)
            return
    assert(False)

def triangles():
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    result = []
    removed = False
    sorted_remain = sorted(range(N), key=lambda x: P[x])
    while len(sorted_remain) >= 3:
        if make_triangle_from_maximal_points(P, sorted_remain, result):
            continue
        a, b = sorted_remain[:2]
        v = vector(P[a], P[b])
        C = set(sorted_remain)
        if not removed:
            removed = True
            remove_unused(P, sorted_remain, C, a, v, result)
        while not len(C) <= 2*(len(sorted_remain)-len(C)):
            for i in result.pop():
                insort(P, sorted_remain, i)
                if outer_product(v, vector(P[a], P[i])) == 0:
                    C.add(i)
        if len(C) == 3 and len(sorted_remain) == 6:
            make_triangles_for_special_case(P, sorted_remain, result)
            continue
        make_triangles_from_max_colinear(P, sorted_remain, C, result)
    return "%s\n%s" % (len(result), "\n".join(map(lambda x: " ".join(map(lambda y: str(y+1), x)), result))) if result else 0

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, triangles()))
