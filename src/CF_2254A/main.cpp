#include <bits/stdc++.h>
using namespace std;

using ll = long long;



int solve() {

    int a, b, c; cin >> a >> b >> c;
    int r = 0;

    //cout << a << ' ' << b << ' ' << c << endl;

    while (a != b && b != c && c != a){

        if (a > b && b > c){
            a--;
            c++;
        }
        else if (b > a && a > c){
            b--;
            c++;
        }
        else if (c > a && a > b){
            c--;
            b++;
        }
        else if (c > b && b > a){
            c--;
            a++;
        }
        else if (b > c && c > a){
            b--;
            a++;
        }
        else if (a > c && c > b){
            a--;
            b++;
        }

        r++;

        //cout << a << ' ' << b << ' ' << c << endl;


    }

    cout << r << '\n';


    return 0;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;

    while(t--) solve();

    return 0;
}
