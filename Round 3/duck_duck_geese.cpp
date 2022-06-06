// Copyright (c) 2022 kamyu. All rights reserved.

/*
 * Google Code Jam 2022 Round 3 - Problem B. Duck, Duck, Geese
 * https://codingcompetitions.withgoogle.com/codejam/round/00000000008779b4/0000000000b45244
 *
 * Time:  O(NlogN)
 * Space: O(N)
 *
 */

#include <bits/stdc++.h>
using namespace std;

template <typename T>
class SegmentTree {
 public:
    explicit SegmentTree(
        int N,
        const function<T(const int&)>& build_fn,
        const function<T(const T&, const T&)>& query_fn,
        const function<T(const T&, const T&)>& update_fn)
      : base_(N),
        tree_(2 * N),
        lazy_(2 * N),
        build_fn_(build_fn),
        query_fn_(query_fn),
        update_fn_(update_fn) {
        H_ = 1;
        while ((1 << H_) < N) {
            ++H_;
        }
        for (int i = base_; i < base_ + N; ++i) {
            tree_[i] = build_fn_(i - base_);
        }
        for (int i = base_ - 1; i >= 1; --i) {
            tree_[i] = query_fn_(tree_[2 * i], tree_[2 * i + 1]);
        }
    }

    void update(int L, int R, const T& val) {
        L += base_;
        R += base_;
        int L0 = L, R0 = R;
        for (; L <= R; L >>= 1, R >>= 1) {
            if ((L & 1) == 1) {
                apply(L++, val);
            }
            if ((R & 1) == 0) {
                apply(R--, val);
            }
        }
        pull(L0);
        pull(R0);
    }

    T query(int L, int R) {
        T result{};
        if (L > R) {
            return result;
        }
        L += base_;
        R += base_;
        push(L);
        push(R);
        for (; L <= R; L >>= 1, R >>= 1) {
            if ((L & 1) == 1) {
                result = query_fn_(result, tree_[L++]);
            }
            if ((R & 1) == 0) {
                result = query_fn_(result, tree_[R--]);
            }
        }
        return result;
    }

 private:
    void apply(int x, const T& val) {
        tree_[x] = update_fn_(tree_[x], val);
        if (x < base_) {
            lazy_[x] = update_fn_(lazy_[x], val);
        }
    }

    void pull(int x) {
        while (x > 1) {
            x >>= 1;
            tree_[x] = query_fn_(tree_[x * 2], tree_[x * 2 + 1]);
            if (!empty(lazy_[x])) {
                tree_[x] = update_fn_(tree_[x], lazy_[x]);
            }
        }
    }

    void push(int x) {
       for (int h = H_; h > 0; --h) {
           int y = x >> h;
           if (!empty(lazy_[y])) {
                apply(y * 2, lazy_[y]);
                apply(y * 2 + 1, lazy_[y]);
                lazy_[y].clear();
            }
        }
    }

    int base_;
    int H_;
    vector<T> tree_;
    vector<T> lazy_;
    const function<T(const int&)> build_fn_;
    const function<T(const T&, const T&)> query_fn_;
    const function<T(const T&, const T&)> update_fn_;
};

int64_t duck_duck_geese() {
    int N, C;
    cin >> N >> C;
    vector<int> A(C), B(C);
    for (int i = 0; i < C; ++i) {
        cin >> A[i] >> B[i];
        if (!A[i]) {
            A[i] = 1;
        }
    }
    vector<int> P(N);
    for (int i = 0; i < N; ++i) {
        cin >> P[i];
        --P[i];
    }
    vector<vector<int>> idx(C);
    for (int i = 0; i < 2 * N; ++i) {
        idx[P[i < N ? i : i - N]].emplace_back(i);
    }
    const auto& build = [](const auto& i) {
        return vector<int>{0, 1};
    };
    const auto& query = [](const auto& x, const auto& y) {
        if (empty(x)) {
            return y;
        }
        if (x[0] != y[0]) {
            return x[0] > y[0] ? x : y;
        }
        return vector<int>{x[0], x[1] + y[1]};
    };
    const auto& update = [](const auto& x, const auto& y) {
        if (empty(x)) {
            return y;
        }
        return vector<int>{x[0] + y[0], x[1]};
    };
    SegmentTree<vector<int>> st(2 * N, build, query, update);
    const auto& add = [&](const auto& idx,
                          const auto& i, const auto& a, const auto& b,
                          const auto& diff) {
        st.update((i - 1 >= 0 ? idx[i - 1] + 1 : 0),
                  (i < size(idx) ? idx[i] - 1 : 2 * N - 1), diff);
        if (i + a - 1 < size(idx)) {
            st.update(idx[i + a - 1],
                      (i + b < size(idx) ? idx[i + b] - 1 : 2 * N - 1), diff);
        }
    };
    vector<int> curr(C);
    for (int c = 0; c < C; ++c) {
        add(idx[c], curr[c], A[c], B[c], vector<int>{+1, 0});
    }
    int64_t result = 0;
    for (int i = 0; i < N; ++i) {
        const auto& ret = st.query(i + 1, i + N - 2);
        if (ret[0] == C) {
            result += ret[1];
        }
        const int c = P[i];
        add(idx[c], curr[c], A[c], B[c], vector<int>{-1, 0});
        ++curr[c];
        add(idx[c], curr[c], A[c], B[c], vector<int>{+1, 0});
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr);
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": " << duck_duck_geese() << '\n';
    }
    return 0;
}
