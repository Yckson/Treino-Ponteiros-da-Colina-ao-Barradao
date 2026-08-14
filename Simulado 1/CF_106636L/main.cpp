#include <bits/stdc++.h>
using namespace std;

using ll = long long;

/*


    A dificuldade nesse problema aqui é perceber a relação matemática.

    1 número igual      = 0 pares
    2 números iguais    = 1 par
    3 números iguais    = 3 pares
    4 números iguais    = 6 pares

                ...
    n números iguais    = (n*(n+1))/2 - 1 - (n-1)

    Eu encontrei durante a prova, você encontra aí no papel com calma.
    Esse tipo de solução aparece quando os estados futuros são determinísticos e calculáveis
    Só tem que ficar atento.



    Tive alguns problemas para submeter:
        1 - esqueci a bosta da fórmula pra somar de 1 até n. Quando lembrei, conseguir modelar a fórmular final.
        2 - usei int primeiro, sendo que a soma estoura 2³²-1. O ideal é usar long long (ll)
        3 - usei unordered_map (que funciona como um hashmap) para contar a quantidade de elementos, mas ele estoura por
            pouco o limite de memória do problema. Isso não costuma acontecer na Maratona da SBC, não esperava por essa.


        4 - a solução abaixo funciona e segue:


*/




void solve (){

    ll n; cin >> n;

    map<ll, ll> p;


    for (ll i = 1; i <= n; i++){

        ll ai; cin >> ai;
        p[ai]++;

    }

    ll cnt = 0;

    for (auto [k, v] : p){
        cnt += (v*(v+1))/2 - 1 - (v-1);
    }

    cout << cnt << '\n';

}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve();

    return 0;
}
