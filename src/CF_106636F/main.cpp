#include <bits/stdc++.h>
#include <cmath>
#include <string>
using namespace std;

using ll = long long;

void solve(){

    string c; cin >> c;

    if (stoll(c) > 9876543210){
        cout << -1 << '\n';
        return;
    }

    int k = c.size();
    unordered_set<char> e;

    string ans = "";
    for (int i = 0; i < k; i++){
        if (e.count(c[i])){
            if (c[i]-'0'+1 >  9){
                ll up = stoll(c.substr(0, i));
                up++;
                up *= pow(10, k - i+1);
                ll down = (i + 1 < k) ? stoll(c.substr(i+1, k - i)) : 0;

                ll t = up + down;
                c = to_string(t);
                k = c.size();
                i = 0;
                e.clear();
                ans = "";
                continue;
            }

            ans.push_back(c[i]+1);
            e.insert(c[i+1]);
        }
        else{
            ans.push_back(c[i]);
            e.insert(c[i]);
        }

    }

    cout << ans << '\n';



}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;

    while (t--) solve();


    return 0;
}
