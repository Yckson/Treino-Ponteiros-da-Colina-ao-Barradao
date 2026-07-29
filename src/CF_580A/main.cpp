//Accepted

#include <bits/stdc++.h>
using namespace std;

using ll = long long;


int solve (){

    int A = 0; int C = 0;

    int n; cin >> n;

    int i; cin >> i;
    int l = i;
    A = 1; C = 1;
    n--;

    while (n--){

        cin >> i;
        if (i >= l){
            C++;
            if (C > A){
                A = C;
            }
        }
        else {
            C = 1;
        }
        l = i;
    }

    cout << A << endl;

    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);



    solve();

    return 0;
}
