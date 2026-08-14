#include <bits/stdc++.h>
using namespace std;

using ll = long long;


void solve (){

    ll n, k; cin >> n >> k;


    ll mk = n / 2;

    if (mk == 0){
        cout << 1 << endl;
        return;
    }

    if (n&1){
        if (k <= mk + 1){
            cout << 2 * k - 1 << endl;
        }
        else{
            cout << 2 * (k - (mk+1)) << endl;
        }
    }
    else{
        if (k <= mk){
            cout << 2 * k - 1 << endl;
        }
        else{
            cout << 2 * (k - mk) << endl;
        }
    }


    //1, 3, 5, 7, 2, 4, 6, 8
    //k = 4


}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve();

    return 0;
}
