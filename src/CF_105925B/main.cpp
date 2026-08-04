#include <bits/stdc++.h>
using namespace std;

#define MAXN 100005

using ll = long long;

int KMP[MAXN][26];
vector<vector<pair<int, char>>> adj;


int mp = 0;
void dfs (int u, int dt, int sw){

    if (dt > 0){
        int peri = dt - sw;
        if (dt % peri == 0 && (dt / peri) >= 2){
            mp = max(mp, peri);
        }
    }

    for (auto [v, a] : adj[u]){

        a = a - 'a';

        for (int c = 0; c < 26; c++){
            if (dt == 0) {
                KMP[dt][c] = 0; 
            } else {
                KMP[dt][c] = KMP[sw][c];
            }
        }

        KMP[dt][a] = dt + 1;

        int ns = KMP[sw][a];

        if (dt == 0){
            ns = 0;
        }

        dfs(v, dt+1, ns);

    }

}

int solve (){

    int n; cin >> n;

    adj = vector<vector<pair<int, char>>> (n+1, vector<pair<int, char>> ());
    vector<int> p (n+1);

    for (int i = 1; i < n; i++){

        int pi; cin >> pi;

        p[i] = pi;

    }

    for (int i = 1; i < n; i++){
        char c; cin >> c;
        adj[p[i]].push_back({i+1, c});
    }


    dfs(1, 0, 0);

    cout << mp << endl;

    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
