#include <bits/stdc++.h>
#include <climits>
using namespace std;

using ll = long long;

/*
    Para resolver esse problema, é necessário ter uma sacada antes.

    Quando ele diz que posso escolher qualquer X em um intervalo, ele quer dizer indiretamente o seguinte:
    Você pode inverter números ímpares em pares e pares em ímpares
    Ímpar + Ímpar = par
    Par + ímpar = ímpar
    Par + par = par

    Então o desafio se torna escolher melhor sub-intervalo do array para inverter que maximiza a quantidade total de pares

    Essa escolha pode fazer com que alguns pares virem ímpar também. Mas se aumentar a quantidade total de pares, tá valendo.

    Sendo assim, usamos uma soma de prefixo para contar quantos números pares temos até i = 0, 1, 2, ... n.
    Calculamos os valores de quantidades de pares e impares nos intervalos:
        qtdpares(r) - qtdpares(l-1) calcula quanto temos no intervalor de l até r
        A quantidade de ímpares é a quantidade total no intervalo - a quantidade de pares

    Verificamos quantos pares ganhamos ou perdemos invertendo o intervalo.
    Se maximizar a quantidade total, consideramos a inversão.

    Como N <= 2*10³, um algoritmo de complexidade O(n²) ainda roda no tempo, permitindo iterar l até n e r até n
    Geralmente evitamos O(n²), mas aqui os limites permitem. É bom ficar atento a isso para não
    perder tempo fazendo overengineering



*/




void solve (){


    ll n; cin >> n;

    vector<ll> prefixa (n+1, 0);



    for (ll i = 1; i <= n; i++){

        int ai; cin >> ai;
        prefixa[i] = !(ai&1) + prefixa[i-1];

    }

    ll mx = prefixa[n];
    for (ll l = 1; l <= n; l++){
        for (ll r = l; r <= n; r++){

            ll qtdp = prefixa[r] - prefixa[l-1];
            ll qtdi = r-l+1 - qtdp;

            ll p = prefixa[n] - qtdp + qtdi;
            if (p > mx){
                mx = p;
                //cout << l << ' ' << r << ' ';
                //cout << mx << endl;
            }
        }
    }
    
    cout << mx << '\n';

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
