#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define MOD 998244353




//dp[i][x][z];


void solve(){

    

    int n; cin >> n;
    string s; cin >> s;
    vector<vector<vector<int>>> dp (n+1, vector<vector<int>>(2, vector<int> (2, 0) ));

    for (int x = 0; x <= 1; x++) for (int y = 0; y <= 1; y++){
        if(s[0] != '?' && s[0] - '0' != x) continue;
        if(s[1] != '?' && s[1] - '0' != y) continue;

        dp[1][x][y] = 1;

    }

    for (int i = 2; i < n; i++){

        for (int x = 0; x <=1; x++) for (int y = 0; y <= 1; y++) for (int z = 0; z <= 1; z++){

            if (s[i] != '?' && s[i]-'0' != z) continue;
            if(x == z) continue;

            dp[i][y][z] = (dp[i][y][z] + dp[i-1][x][y]) % MOD;


        }
    }

    int ans = 0;
    for (int x = 0; x <= 1; x++) for (int y = 0; y <= 1; y++){
        ans = (ans + dp[n-1][x][y]) % MOD;
    }

    cout << ans << '\n';




}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;


    while(t--) solve();

    return 0;
}
