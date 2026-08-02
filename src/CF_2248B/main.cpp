#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

using ll = long long;


int solve (){

    int n, m; cin >> n >> m;

    vector<int> a;
    vector<int> b;

    int t = n;

    

    while (t--){
        int ai; cin >> ai;
        a.push_back(ai);
    }

    t = m;

    sort(a.begin(), a.end());

    while (t--){
        int bi; cin >> bi;
        b.push_back(bi);
    }

    sort(b.begin(), b.end());

    if (n < 2*m) cout << "NO" << '\n';
    else {
        for (int i = 0; i < m; i++){
            if (a[i] >= b[i]){
                cout << "NO" << '\n';
                return 0;
            }
        }

        for (int i = 0; i < m; i++){
            if (a[n-m+i] <= b[i]){
                cout << "NO" << '\n';
                return 0;
            }
        }

        cout << "YES" << '\n';
        
    }

    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;


    while (t--) solve();

    return 0;
}
