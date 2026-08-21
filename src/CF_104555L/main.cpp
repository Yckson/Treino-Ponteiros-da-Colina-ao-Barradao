#include <bits/stdc++.h>
#include <cstddef>
using namespace std;

using ll = long long;



void solve (){

    string s; cin >> s;
    int n = (int) s.size();
    int k; cin >> k;

    vector<vector<char>> ks (k, vector<char>());


    for (int i = 0; i < n; i++){
        ks[i%k].push_back(s[i]);
    }

    

    for (int i = 0; i < k; i++){

        if(!ks[i].empty()) sort(ks[i].begin(), ks[i].end());

    }

    

    string ns;
    vector<int> sk (k, 0);
    for (int i = 0; i < n; i++){
        ns.push_back(ks[i%k][sk[i%k]++]);
    }


    cout << ns << endl;






}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
