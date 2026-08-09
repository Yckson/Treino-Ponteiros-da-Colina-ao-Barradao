#include <algorithm>
#include <bits/stdc++.h>
#include <unordered_map>
#include <vector>
using namespace std;

using ll = long long;

void solve (){


    int n; cin >> n;
    unordered_map<string, pair<int, int>> dict;
    vector<string> order;

    for (int i = 0; i < n; i++){

        string s; int x, y; cin >> s >> x >> y;

        dict[s] = {x,y};
        order.push_back(s);

    }

    vector<string> tre;
    int m; cin >> m;
    for (int i = 0; i < m; i++){
        string si; cin >> si;

        tre.push_back(si);

        
    }


    int q, k; cin >> q >> k;

    while (q--){

        int f; cin >> f;
        vector<string> w;
        for (int i = 0; i < f; i++){
            string si; cin >> si;
            w.push_back(si);
        }

        vector<int> mi;
        bool mc = false;

        int mtk = min(k, f);
        for  (int tk = mtk; tk > 0; tk--){

            int ws = f - tk;
            for (int i = 0; i < m-tk; i++){
                if (w[ws] == tre[i]){
                        int b = 1;
                        int j = 1;
                    for (; j < tk; j++){
                        if(w[ws+j] == tre[i+j]){
                            b++;
                        }
                    }
                    if (b == tk && i+j < m){
                        mi.push_back(i+j);
                        mc = true;
                    }
                }
            }

            if (mc) break;

        }

        for (string& s : w){
            cout << s << ' ';
        }

        if (mc){
            vector<int> si (n, 0);
            for (int i = 0; i < n; i++){
                for (int j : mi){
                    if (dict.count(tre[j])){
                        si[i] += dict[order[i]].first * dict[tre[j]].first + dict[order[i]].second * dict[tre[j]].second;
                    }
                }
            }

            int im = 0;
            int mv = INT_MIN;

            for (int i = 0; i < n; i++){
                if (si[i] > mv){
                    mv = si[i];
                    im = i;
                }
            }

            cout << order[im] << '\n';

        }

        else {
            cout << '*' << '\n';
        }





    }
    





}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    solve ();

    return 0;
}
