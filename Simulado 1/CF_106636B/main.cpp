#include <bits/stdc++.h>
#include <climits>
#include <functional>
#include <queue>
using namespace std;

using ll = long long;

/*

    Pra resolver essa questão, eu pensei no problema como um grafo simplificado

    Desenhe ele para a primeira entrada da seguinte forma: 1 -> 2 
                                                           2 -> 3 
                                                           3 -> 4
                                                           4 -> 1

    O problema diz, de forma simplificada, pra trocar os destinos das areas de dois vértices.
    Bote a cachola pra funcionar pra entender isso.

    No entanto, ele quer que você faça isso com a intenção de tornar o menor ciclo final (após a troca) o maior possível.

    Se temos 3 ciclos de tamanhos: k=1, k=3, k=4. Se fazemos a troca de forma que k=3, k=3, k=4, o menor ciclo será 3.

    Entãp, para resolver o problema, eu implementei um algoritmo para identificar os ciclos e contar seus tamanhos.
    Agrupo do menor para o maior em uma priority queue para pegar os 3 menores ciclos.

    Se eu trocar as areas de quaisquer dois vértices pertencentes a ciclos diferentes, teremos um ciclo maior que os dois
    individualmente.

    Precisamos olhar para o terceiro menor porque se ele for menor do que a união dos dois menores, nosso menor ciclo mínimo
    ainda será o terceiro, já que o problema nos obriga a aplicar a operação uma única vez.



*/


void solve (){

    int n; cin >> n;

    unordered_set<int> s;
    vector<int> g (n+1);

    for (int i = 1; i <= n; i++){

        int v; cin >> v;

        g[i] = v;
        s.insert(i);

    }
    
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int, int>>> pq;
    vector<pair<int,int>> ij;
    while(!s.empty()){

        int v = *s.begin();
        s.erase(v);
        int i = v;
        int j = i;

        
        int u = g[v];
        int ki = 1;

        while (u != v){
            j = u;
            ki++;
            s.erase(u);
            u = g[u];   
        }

        ij.emplace_back(i, j);
        pq.push({ki, ij.size()-1});

    }

    int k1 = pq.top().first; int i1 = ij[pq.top().second].first; int j1 = ij[pq.top().second].second; pq.pop();

    if (pq.size() == 0){
        cout << k1 << ' ' << i1 << ' ' << i1 << '\n';
        return;
    }

    

    int k2 = pq.top().first; int i2 = ij[pq.top().second].first; int j2 = ij[pq.top().second].second; pq.pop();

    if (pq.size() == 0){
        cout << k1+k2 << ' ' << i1 << ' ' << i2<< '\n';
        return;
    }

    int k3 = pq.top().first; int i3 = ij[pq.top().second].first; int j3 = ij[pq.top().second].second; pq.pop();

    int ans = min (k1+k2, k3);

    if (ans == k1+k2){
        cout << k1+k2 << ' ' << i1 << ' ' << i2<< '\n';
        return;
    }
    else{
        cout << k3 << ' ' << i1 << ' ' << i2<< '\n';
        return;
    }






}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    int t; cin >> t;

    while (t--) solve();

    return 0;
}
