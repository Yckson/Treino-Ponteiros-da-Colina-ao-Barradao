#include <bits/stdc++.h>
#include <cctype>
using namespace std;

using ll = long long;


void solve(){

    int n,m; cin >> n >> m;


    bitset<26> s;

    for (int i = 0; i < n; i++){
        string c; cin >> c;
        s |= (1 << (c[0] - 'a'));
    }

    bool p = true;

    for (int i = 0; i < m; i++){

        string c; cin >> c;

        for (char ci : c){
            if (!s.test(tolower(ci)-'a')){
                p = false;
            }
        }
    }

    if (p) cout << "YES";
    else cout << "NO";


    cout << "\n";

}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);



    int t; cin >> t;

    //cout << "!" << endl;


    while (t--) solve();

    return 0;
}
