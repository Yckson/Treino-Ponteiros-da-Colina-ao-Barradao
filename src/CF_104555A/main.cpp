#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve (){

    int n, k; cin >> n >> k;

    int acc = 0;
    for (int i = 0; i < n; i++){

        int ki; cin >> ki;
        if (ki <= k) acc++;
    }


    cout << acc << endl;




}



int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve();

    return 0;
}
