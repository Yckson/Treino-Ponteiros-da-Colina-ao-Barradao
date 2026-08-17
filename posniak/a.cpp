#include <bits/stdc++.h>
#include <climits>

using namespace std;


using ll = long long;

void solve(){

    int n, m; cin >> n >> m;

    vector<int> t (m, INT_MIN);
    for (int i = 0; i < n; i++){

        

        for (int j = 0; j < m; j++){
            int ai; cin >> ai;
            t[j] = max(t[j], ai);
        }


    }

    int sum = 0;
    for (int i = 0; i < m; i++){
        sum += t[i];
    }


    cout << sum << endl;




}

int main (){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();



    return 0;
}