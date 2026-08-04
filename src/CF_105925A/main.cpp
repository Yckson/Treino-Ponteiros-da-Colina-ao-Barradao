#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int solve () {

    int c, g; cin >> c >> g;


    if (c){
        cout << "vivo e morto" << endl;
    }
    else {
        if (g) cout << "vivo" << endl;
        else cout << "morto" << endl;
    }

    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
