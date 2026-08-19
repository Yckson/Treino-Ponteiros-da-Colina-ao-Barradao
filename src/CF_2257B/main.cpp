#include <bits/stdc++.h>
#include <string>
using namespace std;

using ll = long long;

void solve(){

    ll n,m; cin >> n >> m;

    ll m1; cin >> m1;
    string s;
    getline(cin, s);

    ll m2; cin >> m2;

    getline(cin, s);

    ll p1 = m1 + n - 1;
    ll p2 = m2 + m - 1;


    if (p2 > p1) cout << 2 << '\n';
    else cout << 1 << '\n';



}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    ll t; cin >> t;

    while (t--) solve();

    return 0;
}
