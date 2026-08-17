#include <bits/stdc++.h>
using namespace std;




using ll = long long;


void solve (){

    unordered_set<int> s;

    for (int i = 0; i < 10; i++){
        int a; cin >> a; s.insert(a);
    }

    cout << 4 - s.size() << endl;


    
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}
