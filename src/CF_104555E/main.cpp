#include <bits/stdc++.h>
using namespace std;

using ll = long long;

#define endl '\n'

inline int pegar (int f){

    int ans = 0;

    while (f){
        ans += f % 10;
        f /= 10;
    }

    return ans;

}


void solve (){

    int n, k; cin >> n >> k;

    unordered_map<int, int> vc;

    int maior = 0;

    for (int i = 0; i < n; i++){
        int f; cin >> f;

        vc[f]++;
        maior = max(maior, f);

    }

    
    for (int a = maior; a > 0; a--){
        int v = 0;
        v = pegar(a);
        vc[a-v] += vc[a];
        if (vc[a] == 0) continue;
        k -= vc[a];
        if (k <= 0) {
            cout << v << endl;
            return;
        }
    }

    cout << 0 << endl;


}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
