#include <bits/stdc++.h>
using namespace std;

using ll = long long;

vector<char> c (26, 0);


int solve (){

    int n; cin >> n;

    string s; cin >> s;
    string st;

    cout << s << endl;

    if (s.size() == 0){
        cout << 0 << '\n';
        return 0;
    }


    int bs = 0;
    int bss = 0;
    int as = 0;
    int ass = 0;
    int b_ = -1;

    for (int i = 0; i < s.size() - 1; i++){

        if (s[i] == s[i+1]){
            if (ass == 0) as = i;
            ass++;
            if (ass > bss){
                bs = as;
                bss = ass;
            }
        
        }
        else{
            if (i+2 < s.size() && s[i] == s[i+2]){
                if (as == bs){
                    b_ = i+1;
                }
                ass++;
            }
            else {
                if (ass > bss){
                    bs = as;
                    bss = ass;
                }
            }
        }

    }


    st.push_back(s[0]);

    for (int i = 1; i < s.size(); i++){
        if (i == b_) continue;
        if (s[i] != st[st.size()-1]){
            st.push_back(s[i]);
        }
    }

    cout << st.size() << endl;

    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);


    int t; cin >> t;

    while (t--) solve();

    return 0;
}
