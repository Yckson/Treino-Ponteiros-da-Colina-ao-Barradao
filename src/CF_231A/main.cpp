#include <bits/stdc++.h>
using namespace std;

using ll = long long;


void solve (){

    int n; cin >> n;


    int ans = 0;
    while (n--){

        int acc = 0;
        for (int i = 0; i < 3; i++){
            int ci; cin >> ci;
            acc+=ci;
        }

        if (acc >= 2){
            ans++;
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
