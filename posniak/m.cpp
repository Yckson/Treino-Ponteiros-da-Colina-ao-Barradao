#include <bits/stdc++.h>
using namespace std;

using ll = long long;


void solve (){

    int n, k; cin >> n >> k;


    vector<int> p (n+1);
    vector<int> maxi (n+1, 0);
    vector<int> maxv (n+2, 0);

    for (int i = 1; i <= n; i++){

        cin >> p[i];

    }


    for (int i = n; i >= 1; i--){
        
        prefv[i] = p[i] + prefv[i+1];


    }



    
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();


    return 0;
}
