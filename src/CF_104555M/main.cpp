#include <bits/stdc++.h>
using namespace std;

using ll = long long;

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
    for (int u = 1; u <= n; u++){
        for (int v = u+1; v <= n; v++){
            bool r = false;
            for (int m = 1; m <= n; m++){
                if (u == m || v == m) continue;

                if (gp[u][v] > gp[u][m] + gp[m][v]){
                    cout << -1 << endl;
                    return;
                }
                else if (gp[u][v] == gp[u][m] + gp[m][v]){
                    r = true;
                }

            }

            if (r) ans++;

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
