#include <bits/stdc++.h>
#include <queue>
using namespace std;

using ll = long long;

#define endl '\n'

//Não passa no tempo porque k é muito grande e O(klogk é demais)

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

    priority_queue<int, vector<int>, less<int>> pq;

    for (int i = 0; i < n; i++){
        int f; cin >> f;
        pq.push(f);
    }

    for (int i = 0; i < k-1; i++){
        int v = 0;
        if (!pq.empty()){
            int f = 0;
            f = pq.top(); pq.pop();
            v = pegar(f);
            if (f-v != 0) pq.push(f-v);

            
        }
        //cout << "coletou: " << v << endl;

    }

    int v = 0;
    if (!pq.empty()){
        int f = 0;
        f = pq.top(); pq.pop();
        v = pegar(f);
    }

    //cout << "coletou: " << v << endl;
    cout << v << endl;



}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
