#include <bits/stdc++.h>
#include <cstdint>
using namespace std;

using ll = long long;

#define CLEAR(x, n) (x = x & (~(1ULL << (n))))
#define SET(x, n) (x = x | (1ULL << (n)))
#define GET(x, n) (((1ULL << (n)) & (x)) && 1ULL)

int solve (){

    uint64_t x; cin >> x;

    
    //cout << q0 << endl;

    
    uint64_t t = x;
    uint64_t s = x;

    while (1){

        t = s;
        uint64_t q0 = __builtin_clzll(t);
        uint64_t qb = 64 - q0;
        uint64_t p1 = 64 - q0, p2 = 1;

        while (p1 > p2){
            uint64_t t1 = GET(t, p1 - 1);

            if (t1) SET(t, p2 - 1);
            else CLEAR(t, p2 - 1);

            p1--;
            p2++;
        }

        if (t <= x) break;


        
        t = s >> (qb / 2);
        t--;
        if (t < (1ULL << (qb - (qb/2) - 1))) {
            cout << (1ULL << (qb - 1)) - 1 << endl;
            return 0;
        }

        
        s = t << (qb / 2);


    }

    cout << t << endl;


    return 0;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}
