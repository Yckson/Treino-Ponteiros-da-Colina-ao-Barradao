#include <bits/stdc++.h>
using namespace std;

using ll = long long;


void solve (){

    int n; cin >> n;

    vector<int> b (53, 4);

    int j, jj; cin >> j >> jj;
    b[j]--;
    j = min(j, 10);
    b[jj]--;
    j+=min(jj, 10);

    int m, mm; cin >> m >> mm;
    b[m]--;
    m = min(m, 10);
    b[mm]--;
    m+=min(mm, 10);


    int pc = 0;

    for (int i = 0; i < n; i++){
        int c; cin >> c;
        pc += min(c, 10);
        b[c]--;
    }

    b[10] += b[11] + b[12] + b[13];

    j += pc;
    m += pc;

    //cout << j << ' ' << m << endl;

    int pm23 = 23 - m;
    int pj23 = 23 - j;

    int c = min(pm23, pj23);
    //cout << "c: " << c << endl;

    if (c == pm23 && c <= 10){
        if(b[c]){
            cout << c << endl;
            return;
        }

        
    }

    c++;
    while (m + c < 23 && c <= 10){
        if (b[c]){
            cout << c << endl;
            return;
        }
        c++;
    }

    if (m + c == 23 && c <= 10 && b[c]){
        cout << c << endl;
        return;
    }
    
    cout << -1 << endl;


}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve();

    return 0;
}
