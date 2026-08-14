#include <bits/stdc++.h>
using namespace std;

using ll = long long;


void solve (){

    int n, k; cin >> n >> k;


    int mh = 4*60-k;

    int l = 0;
    int r = n;

    int mp = 0;

    while (l <= r){

        int m = l + (r-l)/2;

        if (5 * ((m*(m+1))/2)> mh){
            r = m-1;
        }
        else {
            l = m+1;
            mp = m;
        }
    }


    cout << mp << endl;




}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve();

    return 0;
}
