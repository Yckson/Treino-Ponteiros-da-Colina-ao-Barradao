#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve (){

    int d,c,r; cin >> d >> c >> r;

    vector<int> ac (c+1, 0);

    for (int i = 1; i <= c; i++){
        int ci; cin >> ci;
        ac[i] = ci + ac[i-1];
    }

    for (int i = 0; i < r; i++){
        int ri; cin >> ri;
        d += ri;
    }

    int ans = 0;
    for (int i = 1; i <= c; i++){
        if (d >= ac[i]){
            ans = i;
        }
        else break;
    }

    ans += r;

    cout << ans << endl;



}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
