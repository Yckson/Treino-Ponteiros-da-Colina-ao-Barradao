#include <bits/stdc++.h>
using namespace std;

using ll = long long;




int solve (){

    

    int n, m; cin >> n >> m;

    vector<string> b;

    for (int i = 0; i < n; i++) {

        string s; cin >> s;
        b.push_back(s);

    }

    auto bfs = [&]() -> void {

        queue<pair<int, int>> q;
        int dy[4] = {0, -1, 1, 0};
        int dx[4] = {-1, 0, 0, 1};

        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){

                q.push({i, j});

                while (!q.empty()){

                    auto [y, x] = q.front(); q.pop();

                    bool pb = true;

                    for (int d = 0; d < 4; d++){

                        int ny = y + dy[d];
                        int nx = x + dx[d];

                        if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
                        
                    
                        if (b[ny][nx] == 'B'){
                            pb = false;
                        }

                    }

                    if (b[y][x] == '.'){
                        if (pb) b[y][x] = 'B';
                        else if (b[y][x]) b[y][x] = 'W';
                    }

                }

            }


        }

        return;
    };

    bfs();

    for (string s : b){
        cout << s << '\n';
    }

    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
