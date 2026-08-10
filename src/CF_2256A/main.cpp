#include <algorithm>
#include <array>
#include <bits/stdc++.h>
#include <climits>
using namespace std;

using ll = long long;



void solve (){


    int a,b,c; cin >> a >> b >> c;

    int mi = min({a, b, c});
    int ma = max({a, b, c});

    int r = ma-mi;
    if (!r){
        cout << 0 << '\n';
        return;
    }

    int ra = r;
    do{


        int minp1 = min({b+c, b, c});
        int minp2 = min ({a, a+c, c});
        int minp3 = min({a, b, a+b});

        int maxp1 = max({b+c, b, c});
        int maxp2 = max ({a, a+c, c});
        int maxp3 = max({a, b, a+b});

        int r1 = maxp1 - minp1;
        int r2 = maxp2 - minp2;
        int r3 = maxp3 - minp3;

        int minR = min ({r1, r2, r3});

        if (minR == r1){
            a = b+c;
        }
        else if (minR == r2){
            b = a+c;
        }
        else {
            c = a+b;
        }

        if (ra > minR){
            ra = minR;
        }
        else {
            break;
        }
    }while (1);

    cout << ra << endl;

    


}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    int t; cin >> t;

    while (t--) solve();

    return 0;
}
