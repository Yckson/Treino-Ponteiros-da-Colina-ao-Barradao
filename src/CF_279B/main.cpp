#include <bits/stdc++.h>
using namespace std;

using ll = long long;

//Versão tentando implementar com Binary Search

void solve (){

    int n, t; cin >> n >> t;

    vector<int> a (n+1);
    vector<int> prefix (n+1, 0);
    for (int i = 1; i <= n; i++){
        int ai; cin >> ai;
        a[i] = ai;
        prefix[i] = prefix[i-1] + ai;
    }
    
    int ans = 0;
    for (int i = 1; i<=n; i++){

        int l = i; int r = n;


        while (l <= r){

            int m = l + (r - l) / 2;

            if (prefix[m] - prefix[i - 1] > t){
                r = m-1;
            }
            else{
                ans = max(ans, m-i+1);
                l = m+1;


            }


        }
        
    }

    cout << ans << endl;

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
