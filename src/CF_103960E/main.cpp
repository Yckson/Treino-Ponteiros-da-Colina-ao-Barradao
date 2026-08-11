#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve (){

    int n; cin >> n;
    vector<int> b (n+1);

    for (int i = 1; i <= n; i++){

        int bi; cin >> bi;
        b[i] = bi;

    }

    // for (int i = 1; i <= n; i++){
    //     cout << b[i] << ' ';
    // }

    //cout << endl;

    unordered_map<int, int> arr;
    int ta = 0;

    for (int i = 1; i <= n; i++) {
        if (arr[b[i] + 1] > 0) {
            arr[b[i] + 1]--; 
            arr[b[i]]++;     
        } 
        else {
            ta++;
            arr[b[i]]++;
        }
    }

    cout << ta << '\n';


}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve();
    return 0;
}
