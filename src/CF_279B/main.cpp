#include <bits/stdc++.h>
using namespace std;

using ll = long long;


void solve (){

    int n, t; cin >> n >> t;

    vector<int> a;
    for (int i = 0; i < n; i++){
        int ai; cin >> ai;
        a.push_back(ai);
    }
    
    queue<int> swin;

    int ws = 0;
    int qtd = 0;
    int ans = 0;

    for (int i = n-1; i >= 0; i--){

        while (ws + a[i] > t){
            if (!swin.empty()){
                ws -= (ws + a[i] - swin.front() > 0) ? swin.front() : 0;
                qtd -= (qtd == 0) ? 0 : 1;
                swin.pop();
            }
            else{
                break;
            }
        }

        if (ws + a[i] > t){
            ws = 0;
            continue;
        }

        ws += a[i];
        swin.push(a[i]);
        qtd = swin.size();
        ans = max(ans, qtd);

    }



    cout << ans << endl;

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
