#include <bits/stdc++.h>
using namespace std;

using ll = long long;


int solve() {

    int n; cin >> n;

    vector<vector<int>> p (n+1, vector<int>());

    vector<int> fi;

    for (int i = 1; i <= n; i++){

        int pi; cin >> pi;
        if (pi == -1){
            fi.push_back(i);
        }
        else{
            p[pi].push_back(i);
        }
    }

    //Contador de profundidade

    stack<tuple<int, int>> s;
    int ans = 0;

    for (int pi : fi){

        s.push({pi, 1});

        while (!s.empty()){

            auto [i, g] = s.top(); s.pop();

            //cout << i << ' ' << g << endl;

            ans = max(g, ans);

            for (int v : p[i]){
                s.push({v, g+1});
            }

        }

    }

    cout << ans << endl;

    




    return 0;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve();

    return 0;
}
