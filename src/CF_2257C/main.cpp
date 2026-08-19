#include <bits/stdc++.h>
using namespace std;

using ll = long long;


void solve(){

    int n; cin >> n;
    vector<int> p(n + 1);
    for (int i = 2; i <= n; i++){
        cin >> p[i];
    }
    int m; cin >> m;
    

    vector<int> a(m);
    vector<bool> dum(n + 1, false);
    for (int i = 0; i < m-1; i++){
        cin >> a[i];
        dum[a[i]] = true;
    }


    cin >> a[m-1];
    dum[a[m-1]] = true;

    int u = a[0];
    int r = u;

    while (u != 1){
        int v = p[u];

        if (dum[v]){
            r = v;
        }

        u = v;

    }

    cout << m - 1 << ' ';
    for (int i = 0; i < m; i++){
        if (a[i] != r){
            cout << a[i] << ' ';
        }
    }



    cout << '\n';

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;

    while(t--) solve();


    return 0;
}
