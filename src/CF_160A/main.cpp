#include <bits/stdc++.h>
using namespace std;

using ll = long long;


void solve (){

    int n; cin >> n;

    vector<int> a(n+1);
    vector<int> pa(n+1, 0);


    for (int i = 1; i <= n; i++){
        cin >> a[i];
        
    }

    sort(a.begin(), a.end());

    for (int i = 1; i <= n; i++){
        pa[i] = a[i] + pa[i-1];
    }

    int ans = 0;
    int sum = 0;
    for (int i = n; i >= 1; i--){
        ans++;
        sum += a[i];
        if (sum > pa[i-1]) break;
    }

    cout << ans << endl;

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve();

    return 0;
}
