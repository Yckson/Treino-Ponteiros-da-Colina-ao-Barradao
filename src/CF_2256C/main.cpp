#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve (){

    int n, k; cin >> n >> k;

    string s; cin >> s;


    int r = 0, b = 0;

    for (int i = 0; i < n*2; i++){

        int ia = i-1;

        if (i == 0){
            ia = 2*n-1;
        }

        int in = i+1;
        if (in == 2*n){
            in = 0;
        }

        if (s[i] == '1'){
            int c = 0;
            c += (s[ia] == '1') ? 1 : 0;
            c += (s[in] == '0') ? 1 : 0;

            if (i&1) b += c;
            else r += c;
        }




    }

    cout << r << ' ' << b << '\n';


}



int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;

    while (t--) solve();

    return 0;
}
