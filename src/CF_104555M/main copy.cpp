#include <bits/stdc++.h>
#include <cstdint>
#include <queue>
using namespace std;

using ll = long long;

uint64_t key (pair<int, int>&& p){
    return (((uint64_t) p.first) << 32) | ((uint64_t) p.second); 
}


void solve (){

    int n; cin >> n;

    vector<vector<int>> gp (n+1, vector<int> (n+1));

    for (int u = 1; u <= n; u++){
        for (int v = 1; v <= n; v++){
            int wi; cin >> wi;
            gp[u][v] = wi;
        }
    }


    int ans = 0;
    unordered_set<uint64_t> removed;
    unordered_set<uint64_t> verified;
    for (int u = 1; u <= n; u++){
        for (int v = 1; v <= n; v++){
            if (verified.count(key({u, v})) || verified.count(key({v, u}))) continue;
            verified.insert(key({u, v}));
            if (u == v) continue;
            vector<int>dist (n+1, INT_MAX);
            dist[u] = 0;
            int w = gp[u][v];

            priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int, int>>> pq;

            pq.push({0, u});

            while(!pq.empty()){

                auto [d, ui] = pq.top(); pq.pop();

                if (d > dist[ui]) continue;

                dist[ui] = d;

                if (v == ui) break;


                for (int vi = 1; vi <= n; vi++){
                    int wi = gp[ui][vi];
                    if (ui == u && vi == v) continue;
                    if (ui == vi) continue;
                    if (removed.count(key({ui, vi})) || removed.count(key({vi, ui})));
                    else{
                        if(dist[vi] > d+wi) pq.push({d+wi, vi});
                    }
                }
            }

            // for (int i = 1; i < dist.size(); i++){
            //     cout << dist[i] << ' ';
            // }

            //cout << endl;

            if (w > dist[v]){
                cout << -1 << endl;
                return;
            }
            else if (w == dist[v]){
                ans++;
                //cout << "somou! " << u << ' ' << v << endl;
                removed.insert(key({u, v}));
            }
        }
    }

    cout << ans << endl;






}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve ();

    return 0;
}
