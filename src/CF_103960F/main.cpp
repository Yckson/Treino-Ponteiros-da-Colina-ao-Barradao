#include <bits/stdc++.h>
using namespace std;

using ll = long long;




void solve (){

    

    int n; int c; cin >> n >> c;

    vector<vector<int>> chr (c, vector<int>(26, 0));
    unordered_map<string, int> mp;

    for (int i = 0; i < n; i++){

        string s; cin >> s;
        mp[s]++;

        for (int j = 0; j < c; j++){

            if (s[j] != '*'){

                chr[j][s[j]-'a'] += 1;

            }
            else{
                for (int k = 0; k < 26; k++){
                    chr[j][k]++;
                }
            }

        }

    }

    string ans;

    for (int i = 0; i < c; i++){
        int ma = INT_MIN;
        int mj = 0;

        for (int j = 0; j < 26; j++){
            int m = chr[i][j];

            if (ma < m){
                ma = m;
                mj = j;
            }
            else if (ma == m){
                if (mj > j){
                    mj = j;
                }
            }
            
        }

        ans.push_back('a'+ (char) mj);

    }

    int t = 0;

    for (int i = 0; i < c; i++){
        string st = ans;
        st[i] = '*';

        t+= mp[st];
    }

    cout << ans << ' ' << t << endl;


}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve ();

    return 0;
}
