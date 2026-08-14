#include <bits/stdc++.h>
using namespace std;

/*

    Essa questão é simples demais, não precisava nem explicar o algoritmo em sim.
    Mas de toda forma, consiste em contar a quantidade de cada letra e printar a letra acompanhada da sua quantidade de
    repetições.
    Se houver apenas uma repetição, não mostrar o "1".




*/

using ll = long long;

void solve (){

    string s; cin >> s;



    char lc = s[0];
    int cnt = 1;

    for (int i = 1; i < (int) s.size(); i++){

        char c = s[i];

        if (c == lc){
            cnt++;
        }
        else{
            cout << lc;
            if (cnt >=2 ){
                cout << cnt;
            }
            cnt = 1;
        }

        lc = c;

    }


    if (cnt >= 2){
        cout << lc << cnt;
    }
    else{
        cout << lc;
    }

    cout << endl;



}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve();

    return 0;
}
