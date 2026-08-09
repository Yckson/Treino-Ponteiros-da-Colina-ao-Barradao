#include <bits/stdc++.h>
using namespace std;

using ll = long long;


int solve (){

    int n; cin >> n;

    int la; cin >> la;
    unordered_map<int, int> c;
    vector<int> s (1, 1);
    c[0] = la;

    for (int i = 1; i < n; i++){
        int ai; cin >> ai;

        if (ai == la) s[((int)s.size())-1]++;
        else {
            s.push_back(1);
            c[((int) s.size())-1] = ai;
        }


        la = ai;

    }

    // for (int l : s){
    //     cout << l << ' ';
    // }
    // cout << endl;

    int b = (int) s.size();
    int t = 0;

    for (int i = 1; i < b; i++){
        if (s[i-1] >= 2 && s[i] >= 2){
            t = 2;
            break;
        }
    }

    if (!t){
        for (int i = 0; i < b; i++){
            if (s[i] >= 2){

                bool r = (i + 1 < b) && (i+2>=b || c[i] != c[i+2]);
                bool l = (i - 1 >= 0) && (i-2<0 || c[i] != c[i-2]);


                if (r || l){
                    t = 1;
                    break;
                }

            }
        }
    }

    if (b == 1){
        t = 0;
    }

    cout << b + t << endl;


    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    int t; cin >> t;

    while (t--) solve();

    return 0;
}
