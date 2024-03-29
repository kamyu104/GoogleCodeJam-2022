// Copyright (c) 2022 kamyu. All rights reserved.

/*
 * Google Code Jam 2022 Virtual World Finals - Problem E. Triangles
 * https://codingcompetitions.withgoogle.com/codejam/round/000000000087762e/0000000000b9c555
 *
 * Time:  O(N^2)
 * Space: O(N)
 *
 */

#include <bits/stdc++.h>
using namespace std;

vector<int64_t> vec(const vector<int64_t>& a, const vector<int64_t>& b) {
    return {a[0] - b[0], a[1] - b[1]};
}

int64_t inner_product(const vector<int64_t>& a, const vector<int64_t>& b) {
    return a[0] * b[0] + a[1] * b[1];
}

int ccw(const vector<int64_t>& a, const vector<int64_t>& b, const vector<int64_t>& c) {
    const int64_t v = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]);
    return v == 0 ? 0 : (v > 0 ? 1 : -1);
}

// Return true if t is strictly inside a, b line segment
bool is_strictly_inside_segment(const vector<int64_t>&t,
    const vector<int64_t>& a, const vector<int64_t>& b) {
    return ccw(t, a, b) == 0 && inner_product(vec(a, t), vec(t, b)) > 0;
}

// Return true if t is strictly inside a, b, c triangle
bool is_stricly_inside_triangle(const vector<int64_t>&t,
    const vector<int64_t>& a, const vector<int64_t>& b, const vector<int64_t>& c) {
    const auto d1 = ccw(t, a, b), d2 = ccw(t, b, c), d3 = ccw(t, c, a);
    return (d1 > 0 && d2 > 0 && d3 > 0) || (d1 < 0 && d2 < 0 && d3 < 0);
}

// Return true if t is inside a, b, c triangle
bool is_inside_triangle(const vector<int64_t>&t,
    const vector<int64_t>& a, const vector<int64_t>& b, const vector<int64_t>& c) {
    const auto d1 = ccw(t, a, b), d2 = ccw(t, b, c), d3 = ccw(t, c, a);
    return (d1 >= 0 && d2 >= 0 && d3 >= 0) || (d1 <= 0 && d2 <= 0 && d3 <= 0);
}

bool cross(const vector<int64_t>& a, const vector<int64_t>& b,
    const vector<int64_t>& c, const vector<int64_t>& d) {
    return ccw(a, c, d) * ccw(b, c, d) < 0 && ccw(a, b, c) * ccw(a, b, d) < 0;
}

void insort(const vector<vector<int64_t>>& P, vector<int> *sorted_remain, int x) {
    auto it = begin(*sorted_remain);
    for (; it != end(*sorted_remain); ++it) {
        if (P[*it] > P[x]) {
            break;
        }
    }
    sorted_remain->insert(it, x);
}

void remove_unused(const vector<vector<int64_t>>& P, vector<int> *sorted_remain,
    unordered_set<int> *C, int a, int b) {

    const int cnt = count_if(cbegin(P), cend(P), [&](const auto& p) {
        return ccw(P[a], P[b], p) == 0;
    });
    int remove_cnt = max(cnt - 2 * (static_cast<int>(size(P)) - cnt), 0);
    for (auto it = begin(*C); remove_cnt; --remove_cnt, it = C->erase(it)) {
        sorted_remain->erase(find(begin(*sorted_remain), end(*sorted_remain), *it));
    }
}

int find_nearest_point(const vector<vector<int64_t>>& P, const vector<int>& sorted_remain,
    int x, int y) {

    int64_t d1 = numeric_limits<int64_t>::max(), d2 = numeric_limits<int64_t>::max();
    int z1 = -1, z2 = -1;
    for (const auto& c : sorted_remain) {
        const int64_t side = ccw(P[y], P[x], P[c]);
        if (side == 0) {
            continue;
        }
        const auto& v = vec(P[y], P[c]);
        const auto& d = inner_product(v, v);
        if (side > 0) {
            if (z1 != -1 && ccw(P[y], P[z1], P[c]) == 0) {
                if (d < d1) {
                    d1 = d;
                    z1 = c;
                }
            } else if (z1 == -1 || ccw(P[y], P[z1], P[c]) < 0) {
                d1 = d;
                z1 = c;
            }
        } else {
            if (z2 != -1 && ccw(P[y], P[z2], P[c]) == 0) {
                if (d < d2) {
                    d2 = d;
                    z2 = c;
                }
            } else if (z2 == -1 || ccw(P[y], P[z2], P[c]) > 0) {
                d2 = d;
                z2 = c;
            }
        }
    }
    return z1 != -1 ? z1 : z2;
}

bool make_triangle_from_max_points(const vector<vector<int64_t>>& P, vector<int> *sorted_remain,
    vector<vector<int>> *result) {

    const int x = (*sorted_remain)[size(*sorted_remain) - 1];
    const int y = (*sorted_remain)[size(*sorted_remain) - 2];
    const int z = find_nearest_point(P, *sorted_remain, x, y);
    if (z == -1) {
        return false;
    }
    result->push_back({x, y, z});
    for (const auto& i : result->back()) {
       sorted_remain->erase(find(begin(*sorted_remain), end(*sorted_remain), i));
    }
    return true;
}

void make_triangles_from_max_colinear(const vector<vector<int64_t>>& P, vector<int> *sorted_remain,
    const unordered_set<int>& C,
    vector<vector<int>> *result) {

    vector<int> other, colinear;
    for (const auto& x : *sorted_remain) {
        if (!C.count(x)) {
            other.emplace_back(x);
        } else {
            colinear.emplace_back(x);
        }
    }
    while (size(colinear) >= 2) {
        const int x = colinear.back();
        colinear.pop_back();
        const int y = colinear.back();
        colinear.pop_back();
        const int z = find_nearest_point(P, other, x, y);
        other.erase(find(begin(other), end(other), z));
        result->push_back({x, y, z});
        for (const auto& i : result->back()) {
            sorted_remain->erase(find(begin(*sorted_remain), end(*sorted_remain), i));
        }
    }
}

bool check(const vector<int64_t>& x, const vector<int64_t>& y, const vector<int64_t>& z,
    const vector<int64_t>& a, const vector<int64_t>& b, const vector<int64_t>& c) {

    vector<vector<int64_t>> t1 = {x, y, z}, t2 = {a, b, c};
    if ((accumulate(cbegin(t1), cend(t1), 0, [&](const auto& total, const auto& t) {
             return total + is_stricly_inside_triangle(t, a, b, c);
         }) == 1 &&
         accumulate(cbegin(t1), cend(t1), 0, [&](const auto& total, const auto& t) {
             return total + !is_inside_triangle(t, a, b, c);
         }) == 2) ||
        (accumulate(cbegin(t2), cend(t2), 0, [&](const auto& total, const auto& t) {
             return total + is_stricly_inside_triangle(t, x, y, z);
         }) == 1 &&
         accumulate(cbegin(t2), cend(t2), 0, [&](const auto& total, const auto& t) {
             return total + !is_inside_triangle(t, x, y, z);
         }) == 2)) {
        return false;
    }
    for (const auto& [A, B] : {
        make_pair(x, y), make_pair(y, z), make_pair(z, x)
    }) {
        for (const auto& [C, D] : {
            make_pair(a, b), make_pair(b, c), make_pair(c, a)
        }) {
            if (cross(A, B, C, D) ||
                (ccw(A, C, D) == 0 && ccw(B, C, D) == 0 &&
                 (is_strictly_inside_segment(A, C, D) || is_strictly_inside_segment(B, C, D) ||
                  is_strictly_inside_segment(C, A, B) || is_strictly_inside_segment(D, A, B)))) {
                return false;
            }
        }
    }
    return true;
}

void make_triangles_by_brute_force(const vector<vector<int64_t>>& P, vector<int> *sorted_remain,
    vector<vector<int>> *result) {

    int i = 0;
    for (int j = i + 1; j < size(*sorted_remain); ++j) {
        for (int k = j + 1; k < size(*sorted_remain); ++k) {
            const int x = (*sorted_remain)[i], y = (*sorted_remain)[j], z = (*sorted_remain)[k];
            if (ccw(P[x], P[y], P[z]) == 0) {
                continue;
            }
            vector<int> remain;
            for (const auto& o : *sorted_remain) {
                if (o != x && o != y && o != z) {
                    remain.emplace_back(o);
                }
            }
            const int a = remain[0], b = remain[1], c = remain[2];
            if (ccw(P[a], P[b], P[c]) == 0 || !check(P[x], P[y], P[z], P[a], P[b], P[c])) {
                continue;
            }
            for (const auto& [A, B, C] : {make_tuple(x, y, z), make_tuple(a, b, c)}) {
                result->push_back({A, B, C});
                for (const auto& i : result->back()) {
                    sorted_remain->erase(find(begin(*sorted_remain), end(*sorted_remain), i));
                }
            }
            return;
        }
    }
    assert(false);
}

void triangles() {
    int N;
    cin >> N;
    vector<vector<int64_t>> P(N);
    for (int i = 0; i < N; ++i) {
        P[i].resize(2);
        cin >> P[i][0] >> P[i][1];
    }
    vector<vector<int>> result;
    bool removed = false;
    vector<int> sorted_remain(N);
    iota(begin(sorted_remain), end(sorted_remain), 0);
    sort(begin(sorted_remain), end(sorted_remain), [&](const auto& a, const auto& b) {
        return P[a] < P[b];
    });
    while (size(sorted_remain) >= 3) {
        if (make_triangle_from_max_points(P, &sorted_remain, &result)) {
            continue;
        }
        const int a = sorted_remain[0], b = sorted_remain[1];
        unordered_set<int> C(cbegin(sorted_remain), cend(sorted_remain));
        if (!removed) {
            removed = true;
            remove_unused(P, &sorted_remain, &C, a, b);
            if (empty(sorted_remain)) {
                break;
            }
        }
        for (; size(C) / 2 > (size(sorted_remain) - size(C)); result.pop_back()) {
            for (const auto& i : result.back()) {
                insort(P, &sorted_remain, i);
                if (ccw(P[a], P[b], P[i]) == 0) {
                    C.emplace(i);
                }
            }
        }
        if (size(C) == 3 && size(sorted_remain) == 6) {
            make_triangles_by_brute_force(P, &sorted_remain, &result);
            break;
        }
        make_triangles_from_max_colinear(P, &sorted_remain, C, &result);
    }
    cout << size(result) << '\n';
    if (!empty(result)) {
        for (const auto& x : result) {
            cout << x[0] + 1 << ' ' << x[1] + 1 << ' ' << x[2] + 1 << '\n';
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": ";
        triangles();
    }
    return 0;
}
