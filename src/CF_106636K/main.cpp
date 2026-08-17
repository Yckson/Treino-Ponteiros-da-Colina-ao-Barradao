#include <algorithm>
#include <bits/stdc++.h>
#include <cmath>
#include <cstdint>

using namespace std;

using ll = long long;


vector<ll> dp;

void dfs (){

    stack<pair<ll, uint32_t>> s;

    s.push({0,0});

    while (!s.empty()){

        auto [n, m] = s.top(); s.pop();

        if (n != 0){
            dp.push_back(n);
        }


        for (int d = 0; d <= 9; d++){

           if (n == 0 && d == 0) continue;
           if (m & (1 << d)) continue;

           ll nn = n * 10 + d;

           if (nn > 9876543210LL) continue;

           s.push({nn, m | (1 << d)});

        }

    }
}

void solve (){

    //exit(2);
    ll c; cin >> c;

    if (c > 9876543210){
        cout << -1 << '\n';
        return;
    }

    ll ans = *lower_bound(dp.begin(), dp.end(), c);

    cout << ans - c << '\n';

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    
    dfs();
    //exit(3);
    sort(dp.begin(), dp.end());

    while (t--) solve();


    return 0;
}
