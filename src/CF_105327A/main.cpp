#include <bits/stdc++.h>
using namespace std;

using ll = long long;




void solve (){

    exit(0);

    int n; cin >> n;
    int k; cin >> k;


    k -= n-1;

    int ans = max (1, k/n);

    cout << ans << endl;


    

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
