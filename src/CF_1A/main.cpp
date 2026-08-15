#include <bits/stdc++.h>
using namespace std;

using ll = long long;


void solve (){


    ll n,m,a; cin >> n >> m >> a;

    n += (n%a != 0)?(a - n%a):0;
    m += (m%a != 0)?(a - m%a):0;

    if (n*m <= a*a){
        cout << 1 << endl;
        return;
    }

    cout << (n*m)/(a*a) << endl;



}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve();

    return 0;
}
