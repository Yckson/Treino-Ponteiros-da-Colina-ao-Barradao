#include <bits/stdc++.h>
#include <iterator>
using namespace std;

using ll = long long;


int solve () {

    string s; cin >> s;

    for (int i = 0; i < s.size(); i++){
        if (s[i] == '0') {
            s.erase(i, 1);
            break;
        }
    }

    for (int i = 0; i < s.size(); i++){
        if (s[i] == '1'){
            s.erase(i, 1);
            break;
        }
    }

    cout << s << '\n';


    return 0;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;

    while (t--) solve();
    return 0;
}
