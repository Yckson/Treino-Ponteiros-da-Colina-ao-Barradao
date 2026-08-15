#include <bits/stdc++.h>
using namespace std;

using ll = long long;

/*

    Resolvi refazer essa questão. A abordagem de testar todas as cartas que ainda estão no baralho é melhor
    porque é mais fácil de implementar e as restrições permitem.

*/


void solve (){

    int n; cin >>n;

    map<int, int> b;

    for (int i = 1; i <= 13; i++){
        b[i] += 4;
    }

    int cj, pj;
    cin >> cj; pj = (cj > 10) ? 10 : cj;
    b[cj]--;
    cin >> cj; pj += (cj > 10) ? 10 : cj; 
    b[cj]--;

    int cm, pm;
    cin >> cm; pm = (cm > 10) ? 10 : cm;
    b[cm]--;
    cin >> cm; pm += (cm > 10) ? 10 : cm;
    b[cm]--;

    for (int i = 0; i < n; i++){
        int c; cin >> c;
        b[c]--;
        pm += (c > 10) ? 10 : c;
        pj += (c > 10) ? 10 : c;
    }


    for (auto [c, q] : b){
        int t = (c > 10) ? 10 : c;

        if (q){

            if (pm + t == 23){
                cout << c << endl;
                return;
            }
            else if (pj + t > 23 && pm + t < 23){
                cout << c << endl;
                return;
            }

        }
    }

    cout << -1 << endl;
    


}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve();

    return 0;
}
