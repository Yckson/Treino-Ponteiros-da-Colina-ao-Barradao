#include <bits/stdc++.h>
#include <iomanip>
using namespace std;

using ll = long long;


int solve (){

    int n; cin >> n;


    string s; cin >> s;
    string t; cin >> t;

    int q = 0, r = 0;

    for (int i = 0; i < n; i++){

        if (s[i] == '*'){
            q++;
            if (t[i] != '*'){
                r++;
            }
        }
    }

    double p = r / (double) q;

    cout << std::fixed << std::setprecision(2) << p << endl;


    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}
