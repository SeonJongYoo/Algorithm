// 가장 긴 증가하는 부분수열 4

#include <iostream>
#include <vector>
using namespace std;

int n;
const int MAX = 1001;
int A[MAX];
int dp[MAX];
int parent[MAX];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> A[i];
    dp[0] = 1;
    for (int i = 1; i < n; i++) {
        int tmp = A[i];
        for (int j = i-1; j > -1; j--) {
            if (tmp > A[j]) {
                if (dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    parent[i] = j;
                }
            } else if (dp[i] == 0) {
                dp[i] = 1; 
                parent[i] = i;
            }
        }
    }
    int res = 0, idx = 0;
    for (int i = 0; i < n; i++) {
        if (dp[i] > res) {
            idx = i;
            res = dp[i];
        }
    }
    vector<int> v;
    vector<int>::reverse_iterator rit;
    while (idx != parent[idx]) {
        v.push_back(A[idx]);
        idx = parent[idx];
    }
    v.push_back(A[idx]);

    cout << res << "\n";
    for (rit = v.rbegin(); rit != v.rend(); rit++) cout << *rit << " ";
    return 0;
}