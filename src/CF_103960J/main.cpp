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
    cin >> cj; pj = cj;b[cj]--;

    cin >> cj; pj += cj; b[cj]--;

    int cm, pm;
    cin >> cm; pm = cm;b[cm]--;
    cin >> cm; pm += cm;b[cm]--;

    for (int i = 0; i < n; i++){
        int c; cin >> c;
        b[c]--;
        pm += c;
        pj += c;
    }


    for (auto [c, q] : b){
        int t = (c == 11 || c == 12 || c == 13) ? 10 : c;

        if (q){

            if (pm + t == 23){
                cout << t << endl;
                return;
            }
            else if (pj + t > 23 && pm + t < 23){
                cout << t << endl;
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
