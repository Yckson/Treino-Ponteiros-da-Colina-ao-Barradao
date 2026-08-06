#include <bits/stdc++.h>
using namespace std;

using ll = long long;



int solve(){

    int n; cin >> n;
    vector<int> b (n+1);
    for (int i = 1; i <= n; i++) cin >> b[i];
    sort(b.begin(), b.end());

    int m; cin >> m;
    vector<int> g (m+1);
    for (int i = 1; i <= m; i++) cin >> g[i];
    sort(g.begin(), g.end());

    vector<vector<int>> dp (n+1, vector<int> (m+1, 0));

    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= m; j++){

            int ma = max(dp[i-1][j], dp[i][j-1]);

            if (abs(b[i] - g[j]) <= 1) ma = max(ma, dp[i-1][j-1] + 1);

            dp[i][j] = ma;
        }
    }


    cout << dp[n][m] << endl;




    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
