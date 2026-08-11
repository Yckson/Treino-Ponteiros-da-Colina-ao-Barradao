#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

using ll = long long;


void solve(){


    int n, q; cin >> n >> q;

    vector<ll> a (n+1);

    for (int i = 1; i <= n; i++){

        ll ai; cin >> ai;
        a[i] = ai;
    }

    vector<ll> diff (n+2, 0);

    for (int i = 0; i < q; i++){
        ll l,r; cin >> l >> r;

        diff[l]++;
        diff[r+1]--;

    }

    // diff = {0, 0, 1, 0, 0, 0, -1, 0} por exemplo, demarca as bordas

    for (int i = 1; i < n+2; i++){
        diff[i] = diff[i] + diff[i-1];
    }

    sort(a.begin()+1, a.end());
    sort(diff.begin()+1, diff.end()-1);

    ll sum = 0;
    for (int i = 1; i<=n; i++){
        sum += a[i] * diff[i];
    }

    cout << sum << endl;


}




int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve();

    return 0;
}
