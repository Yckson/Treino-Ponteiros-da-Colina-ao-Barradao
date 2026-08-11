#include <bits/stdc++.h>
#include <bitset>
#include <cstdint>
#include <iostream>
using namespace std;

using llu = unsigned long long;


#define g(k) (1ULL << (k))

void solve (){

    int n, x, y; cin >> n >> x >> y;

    int ans = n - 1 - __builtin_ctzll(x);

    cout << ans << endl;



}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
