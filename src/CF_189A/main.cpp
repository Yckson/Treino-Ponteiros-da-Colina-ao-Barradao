#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int solve(){


    int n; cin >> n;
    int a, b, c; cin >> a >> b >> c;

    vector<int> dp (n+1, -1);
    dp[0] = 0;

    for (int i = 1; i <= n; i++){

        if (i - a >= 0 && dp[i-a] != -1){
            dp[i] = dp[i-a] + 1;
        }

        if (i - b >= 0 && dp[i-b] != -1){
            dp[i] = max(dp[i], dp[i-b]+1);
        }

        if (i - c >= 0 && dp[i-c] != -1){
            dp[i] = max(dp[i], dp[i-c]+1);
        }
    }

    cout << dp[n] << endl;

    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve();

    return 0;
}
