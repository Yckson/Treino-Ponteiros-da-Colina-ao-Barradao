#include <bits/stdc++.h>
#include <climits>
using namespace std;

using ll = long long;


void solve (){

    int n, k; cin >> n >> k;

    vector<int> v (n+1, 0);
    vector<int> mve (n+1, 0);
    mve[0] = INT_MAX;
    vector<int> mie (n+2, 0);
    vector<int> mvd (n+2, 0);
    mvd[n+1] = INT_MAX;

    vector<int> mid (n+1, 0);

    for (int i = 1; i <= n; i++){
        int x; cin >> x;
        v[i] = x;
        if (mve[i-1] > x){
            mve[i] = x;
            mie[i] = i;
        }
        else{
            mve[i] = mve[i-1];
            mie[i] = mie[i-1];
        }
    }

    for (int i = n; i >= 0; i--){
        if(mvd[i+1] > v[i]){
            mvd[i] = v[i];
            mid[i] = i;
        }
        else {
            mvd[i] = mvd[i+1];
            mid[i] = i+1;
        }
    }

    
    int ans = 0;
    multiset<int> j;

    for (int i = 1; i <= n; i++){

        j.insert(v[i] + i);

        if (i > k){
            j.erase(j.find(v[i-k]+(i-k)));
        }

        int mz3 = *j.begin() + k - i;
        int mz1 = mvd[i+1];
        int mz2 = (i>k)? mve[i-k] : INT_MAX;
        
        int mm = min ({mz1, mz2, mz3});
        ans = max(ans, mm);

    }

    cout << ans << endl;

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
