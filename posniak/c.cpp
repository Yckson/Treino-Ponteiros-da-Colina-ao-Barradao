#include <bits/stdc++.h>
using namespace std;

using ll = long long;


void solve (){

    int n; cin >> n;
    int x = 0;
    for (int i = 0; i < n+1; i++){

        x <<= 1;
        int a; cin >> a;
        x |= a;

        //cout << x << ' ' << a << endl;
        
    }

    //cout << x << endl;
    int c = 0;
    while (x != 1){

        if (x&1){
            x = (x<<1) ^ (x ^ 1);
        }
        else {
            x >>= 1;
        }

        c++;

    }

    cout << c << endl;





}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve();

    return 0;
}
