#include <bits/stdc++.h>
using namespace std;

using ll = long long;


void solve (){

    int n; cin >> n;
    string s; cin >> s;

    int cnt = 0;
    int ans = 0;
    for (int i = 0; i < n; i++){

        if (s[i] == 'a') cnt++;
        else{
            if (cnt >= 2){
                ans += cnt;
            }
            cnt = 0;
        }

    }

    if (cnt >= 2) ans += cnt;

    cout << ans << endl;
    

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
