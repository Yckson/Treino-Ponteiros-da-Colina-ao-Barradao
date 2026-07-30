#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int solve (){


    int n, t; cin >> n >> t;

    vector<int> P (n+1);

    for (int i = 1; i < n; i++){

        int a; cin >> a;
        P[i] = i + a;
    }

    vector<char> visited(n+1, false);
    int r = n;
    bool ans = false;

    auto dfs = [&visited, &P, &r, &ans, &t] (auto& self, int i) -> void {

        if (visited[i] || ans) return;
        visited[i] = true;

        if (i == t){
            ans = true;
            return;
        }

        self(self, P[i]);
        
    };

    dfs(dfs, 1);

    if (ans){
        cout << "YES" << endl;
    }
    else{
        cout << "NO" << endl;
    }

    return 0;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve();

    return 0;
}
