#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve (){

    int n; cin >> n;

    for (int i = 1; i <= n; i++){
        int q; cin >> q;
    }

    int m; cin >> m;

    using edge = tuple<int, int, int>;

    vector<edge> es;

    for (int i = 0; i < m; i++){
        int w, u, v; cin >> u >> v >> w;
        es.emplace_back(w, u, v);
    }

    sort(es.begin(), es.end());

    vector<int>pa (n+1);
    vector<int>sz (n+1, 1);
    iota(pa.begin(), pa.end(), 0);


    auto find = [&pa] (auto&& self, int i) -> int {

        if (i == pa[i]) return i;

        return pa[i] = self(self, pa[i]);

    };

    auto uni = [&pa, &sz, &find] (int a, int b) -> bool {

        a = find(find, a); b = find(find, b);

        if (a == b) return false;

        if (sz[a] > sz[b]) swap(a, b);
        pa[a] = b;
        sz[b] += sz[a];

        return true;

    };

    
    
    vector<bool> hs (n+1, false);
    
    int se = 0;
    int c = 0;

    for (auto& e : es){
        auto [w, u, v] = e;

        if (hs[v]) continue;
        if (find(find, u) == find(find, v)) continue;
        

        c += w;
        uni(u, v);
        se++;
        hs[v] = true;
    }

    if (se != n-1){
        cout << -1 << endl;
    }
    else{
        cout << c << endl;
    }


}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}
