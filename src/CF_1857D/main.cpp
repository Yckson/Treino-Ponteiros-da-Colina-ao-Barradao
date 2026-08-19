#include <bits/stdc++.h>
using namespace std;

using ll = long long;

void solve(){

    int n; cin >> n;

    vector<ll> a (n+1);
    vector<ll> b (n+1);


    for (int i = 1; i <= n; i++) cin >> a[i];
    for (int i = 1; i <= n; i++) cin >> b[i];



    vector<vector<ll>> gp (n+1, vector<ll>());

    for (int u = 1; u <= n; u++){
        for (int v = 1; v <= n; v++){

            if (u != v){
                if (a[u]-a[v] >= b[u]-b[v]){
                    gp[u].push_back(v);
                }
            }

        }
    }

    vector<int> eval (n+1, -1);
    bitset<2*100010> visited;

    auto dfs = [&] (auto&& self, ll v) -> int {

        if (visited.test(v)) return 0;
        else if (eval[v] != -1){
            visited.set(v);
            return eval[v];
        }


        int sum = 1;

        for (ll u : gp[v]){
            sum += self(self, u);
        }

        visited.set(v);
        eval[v] = sum;
        return sum;

    };


    int ans_sum = 0;
    
    set<ll> ans_c;
    for (int i = 1; i <= n; i++){
        

        int t = dfs(dfs, i);
        cout << t << endl;
        if (t == n){
            ans_sum++;
            ans_c.insert(i);
        }
        
        visited.reset();
    }

    

    cout << ans_sum << '\n';

    exit(2);

    for (auto it = ans_c.begin(); it != ans_c.end(); ++it){

        cout << *it << ' ';

    }

    cout << '\n';




}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t; cin >> t;

    while (t--) solve();

    return 0;
}
