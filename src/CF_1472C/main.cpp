#include <bits/stdc++.h>
using namespace std;

using ll = long long;



int solve () {

    int n; cin >> n;


    vector<vector<int>> adj (n+2, vector<int>());
    vector<int> s (n+2, 0);

    for (int i = 1; i <= n; i++){

        int a; cin >> a;

        int d = a + i;
        s[i] = a;

        adj[((d > n) ? n+1 : d)].push_back(i);

    }

    // for (int i = 1; i <= n+1; i++){
    //     cout << i << ": { ";
    //     for (int v : adj[i]){
    //         cout << v << " ";
    //     }
    //     cout << "}" << endl;
    // }

    vector<int> visited (n+2, -1);


    auto dfs = [&](auto& self, int u) -> int {

        if (visited[u] != -1) return visited[u];

        

        int m = 0;

        for (int v : adj[u]){
            m = max(self(self, v), m);
        }

        visited[u] = s[u] + m;
        //cout << u << " ";
        //cout << "-> " << m << endl;

        return visited[u];

    };

    cout << dfs(dfs, n+1) << endl;




    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;


    while (t--) solve();

    return 0;
}
