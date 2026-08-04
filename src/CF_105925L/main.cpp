#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int solve (){

    ll m; cin >> m;

    m = m * 1000000 * 8;

    int q = 64 - __builtin_clzll(m);
    cout << q << endl;

    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
