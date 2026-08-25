#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve (){

    int y, w; cin >> y >> w;

    int a = max(y, w);

    int n = 6-a+1;
    int g = gcd(n,6);

    cout << n/g << '/' << 6/g << endl;

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
