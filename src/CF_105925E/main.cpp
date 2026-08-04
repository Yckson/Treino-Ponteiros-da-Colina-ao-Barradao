#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int solve (){

    int y, k; cin >> y >> k;

    int x = 1;
    while (k--){
        x = x + gcd(x, y);
    }

    cout << x << endl;

    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
