#include <bits/stdc++.h>
using namespace std;

using ll = long long;


void solve (){

    ll n; cin >> n;


    ll ci = 0, cp = 1;
    ll psum = 0;
    ll ans = 0;
    for (ll i = 0; i < n; i++){
        ll t = 0; cin >> t;

        psum += t&1;
        if (psum&1){
            ans += cp;
            ci++;
        }
        else {
            ans += ci;
            cp++;
        }

    }

    cout << ans << endl;





}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);



    solve ();

    return 0;
}
