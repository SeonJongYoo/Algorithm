// 소수 찾기

#include <iostream>
#include <vector>
using namespace std;

const int MAX = 1001;
int num[MAX] = {0, };

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    for (int i = 2; i < MAX; i++) {
        if (num[i] == 0) {
            for (int j = i*i; j < MAX; j += i) {
                num[j] = 1;
            }
        }
    }

    vector<int> v;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int input;
        cin >> input;
        v.push_back(input);
    }

    int res = 0;
    vector<int>::iterator it;
    for (it = v.begin(); it != v.end(); it++) {
        if (*it == 1) continue;
        if (num[*it] == 0) res++;
    }
    cout << res;
    
    return 0;
}