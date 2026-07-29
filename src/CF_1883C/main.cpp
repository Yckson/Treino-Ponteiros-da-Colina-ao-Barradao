#include <bits/stdc++.h>
using namespace std;

#define INF INT_MAX

using ll = long long;




int solve (){

    int n, k; cin >> n >> k;



    int m = INF; int o = 0;

    int ai;

    while (n--){
        cin >> ai;

        int r = ai % k;
        m = (r == 0) ? 0 : min(m, k - r);
        o += !(ai & 1);
    }

    int ans;
    if (k == 4){
        int t;
        if (o >= 2) t = 0;
        else if (o > 0) t = 1;
        else t = 2;

        ans = min (t, m);
    }
    else {
        ans = m;
    }

    cout << ans << '\n';
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    int t; cin >> t;
    while (t--) solve();

    return 0;
}
