#include <bits/stdc++.h>
using namespace std;

using ll = long long;

vector<int> prime (200100, -1);


int solve() {

    int n; cin >> n;
    n++;
    //cout << n << endl;

    if (prime[n] != -1){
        if (prime[n]) cout << "YES" << endl;
        else cout << "NO" << endl;
        return 0;
    }

    if (n % 2 && n % 3){
        for (int i = 3; i*i <= n; i+=2){
            if (n % i == 0){
                prime[n] = 0;
                cout << "NO" << endl;
                return 0;
            }
        }
        prime[n] = 1;
    }
    else{
        cout << "NO" << endl;
        return 0;
    }
    

    cout << "YES" << endl;
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;
    prime[2] = 1;
    prime[3] = 1;
    while (t--) solve();

    return 0;
}
