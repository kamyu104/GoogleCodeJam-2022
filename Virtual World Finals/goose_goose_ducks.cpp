// Copyright (c) 2022 kamyu. All rights reserved.

/*
 * Google Code Jam 2022 Virtual World Finals - Problem B. Goose, Goose, Ducks
 * https://codingcompetitions.withgoogle.com/codejam/round/000000000087762e/0000000000b9ce14
 *
 * Time:  O(N + M + S * (logM + logS))
 * Space: O(N + S)
 *
 */

#include <bits/stdc++.h>
using namespace std;

using Location = array<int, 3>;
using Statement = pair<Location, int>;

vector<int> strongly_connected_components(const vector<vector<int>>& adj) {
    int index_counter = 0;
    vector<int> index(size(adj), -1), lowlinks(size(adj), -1), stack;
    vector<bool> stack_set(size(adj));
    vector<int> result(size(adj));
    const auto& iter_strongconnect = [&](int v) {
        vector<vector<int>> stk = {{1, v}};
        while (!empty(stk)) {
            const auto args = move(stk.back());
            stk.pop_back();
            if (args[0] == 1) {
                const int v = args[1];
                index[v] = lowlinks[v] = index_counter++;
                stack_set[v] = true;
                stack.emplace_back(v);
                stk.push_back({4, v});
                for (const auto& w : adj[v]) {
                    stk.push_back({2, v, w});
                }
            } else if (args[0] == 2) {
                const int v = args[1], w = args[2];
                if (index[w] == -1) {
                    stk.push_back({3, v, w});
                    stk.push_back({1, w});
                } else if (stack_set[w]) {
                    lowlinks[v] = min(lowlinks[v], index[w]);
                }
            } else if (args[0] == 3) {
                const int v = args[1], w = args[2];
                lowlinks[v] = min(lowlinks[v], lowlinks[w]);
            } else if (args[0] == 4) {
                const int v = args[1];
                if (lowlinks[v] != index[v]) {
                    continue;
                }
                int w = -1;
                while (w != v) {
                    w = stack.back();
                    stack.pop_back();
                    stack_set[w] = false;
                    result[w] = v;
                }
            }
        }
    };
    for (int v = 0; v < size(adj); ++v) {
        if (index[v] == -1) {
            iter_strongconnect(v);
        }
    }
    return result;
}

bool check(const Location& a, const Location& b) {
    return 1ULL * (a[0] - b[0]) * (a[0] - b[0]) >=
           1ULL * (a[1] - b[1]) * (a[1] - b[1]) + 1ULL * (a[2] - b[2]) * (a[2] - b[2]);
}

void add_statement(const Statement& s, set<Statement> *bst, vector<bool> *is_duck) {
    const auto it = bst->emplace(s).first;
    while (it != begin(*bst) && !check(prev(it)->first, s.first)) {
        (*is_duck)[prev(it)->second] = true;
        bst->erase(prev(it));
    }
    while (next(it) != end(*bst) && !check(next(it)->first, s.first)) {
        (*is_duck)[next(it)->second] = true;
        bst->erase(next(it));
    }
}

int bfs(const vector<vector<int>>& adj, vector<bool> *is_duck) {
    vector<int> q;
    for (int u = 0; u < size(*is_duck); ++u) {
        if ((*is_duck)[u]) {
            q.emplace_back(u);
        }
    }
    while (!empty(q)) {
        vector<int> new_q;
        for (const auto& u : q) {
            for (const auto& v : adj[u]) {
                if ((*is_duck)[v]) {
                    continue;
                }
                (*is_duck)[v] = true;
                new_q.emplace_back(v);
            }
        }
        q = move(new_q);
    }
    return count(cbegin(*is_duck), cend(*is_duck), true);
}

int goose_goose_ducks() {
    int N, M, S;
    cin >> N >> M >> S;
    vector<vector<int>> P(N);
    vector<Location> meetings(M);
    for (int i = 0; i < M; ++i) {
        int X, Y, C;
        cin >> meetings[i][1] >> meetings[i][2] >> meetings[i][0];
    }
    vector<bool> is_duck(N);
    vector<vector<int>> adj(N);
    vector<set<Statement>> bsts(N);
    for (int _ = 0; _ < S; ++_) {
        int A, B;
        int U, V, D;
        cin >> A >> B >> U >> V >> D;
        --A, --B;
        Statement s = {{D, U, V}, A};
        const auto cit = lower_bound(cbegin(meetings), cend(meetings), s.first);
        if ((cit != cbegin(meetings) && !check(*prev(cit), s.first)) ||
            (cit != cend(meetings) && !check(*cit, s.first))) {
            adj[B].emplace_back(A);
        }
        add_statement(s, &bsts[A], &is_duck);
        add_statement(s, &bsts[B], &is_duck);
    }
    if (count(cbegin(is_duck), cend(is_duck), true)) {
        return bfs(adj, &is_duck);
    }
    const auto& components = strongly_connected_components(adj);
    vector<bool> is_candidate(N, true);
    unordered_map<int, int> cnt;
    for (int u = 0; u < N; ++u) {
        ++cnt[components[u]];
        for (const auto& v : adj[u]) {
            if (components[v] != components[u]) {
                is_candidate[components[u]] = false;
                break;
            }
        }
    }
    int result = N;
    for (const auto& [k, v] : cnt) {
        if (is_candidate[k]) {
            result = min(result, v);
        }
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": " << goose_goose_ducks() << '\n';
    }
    return 0;
}
