#include <bits/stdc++.h>
#include <climits>
using namespace std;

using ll = long long;

int solve (){

    int n; cin >> n;

    int ao; int bo;

    cin >> ao >> bo;

    vector<int> d;


    for (int i = 0; i < n-1; i++){

        int a, b; cin >> a >> b;

        d.push_back(abs(a - ao) + abs(b - bo));

        ao = a;
        bo = b;

    }

    int L = 0; int R = INT_MAX;

    int prefixd = 0;

    for (int i = 0; i < (int) d.size(); i++){
        if (!(i & 1)){
            R = min (R, prefixd + d[i]);
            prefixd += d[i];
        }
        else {
            L = max(L, prefixd - d[i]);
            prefixd -= d[i];
        }
    }


    if (L < R - 1) cout << R - 1;
    else cout << -1;

    cout << endl;



    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve ();

    return 0;
}
