#include <bits/stdc++.h>

#define INF INT_MAX


using namespace std;

using ll = long long;


int solve () {

    int n, k; cin >> n >> k;

    int j = 1, A = INF;

    vector<int> p;
    p.push_back(0);
    vector<int> areas;
    areas.push_back(0);
    int t_a = 0;

    for (int i = 1; i <= n; i++){
        int ai; cin >> ai;
        t_a += ai;
        p.push_back(ai);
        areas.push_back(t_a);
    }

    for (int i = 1; i <= n - k + 1; i++){
        int ai = areas[i + k - 1] - areas[i - 1];
        
        if (ai <= A){
            A = ai;
            j = i;
        }
    }

    cout << j << endl;



    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    return solve();
}
