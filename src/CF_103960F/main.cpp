#include <bits/stdc++.h>
using namespace std;

using ll = long long;




void solve (){


    int n, c; cin >> n >> c;

    unordered_map<string, int> d;


    for (int i = 0; i < n; i++){
        string s; cin >> s;
        auto k = s.find('*');
        if (k == s.npos){
            d[s]++;
            continue;
        }

        for (char j = 0; j < 26; j++){

            string t = s;
            t[k] = 'a'+j;
            d[t]++;

        }

    }

    char t = 'z'+1;
    string ans;
    for (int i = 0; i < c; i++){
        ans.push_back(t);
    }
    int cnt = 0;

    for (auto& [s, q] : d){
        if (q > cnt){
            ans = s;
            cnt = q;
        }
        else if (q == cnt){
            if (s < ans){
                ans = s;
            }
        }
    }

    cout << ans << ' ' << cnt << endl;

   

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve ();

    return 0;
}
