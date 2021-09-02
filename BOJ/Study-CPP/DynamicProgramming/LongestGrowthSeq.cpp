// 가장 긴 증가하는 부분수열

#include <iostream>
using namespace std;

int n;
const int MAX = 1001;
int A[MAX];
int dp[MAX];

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
                if (dp[j] + 1 > dp[i]) dp[i] = dp[j] + 1;
            } else {
                if (dp[i] < 1) dp[i] = 1;
            }
        }
    }
    int res = 0;
    for (int i = 0; i < n; i++) {
        if (dp[i] > res) res = dp[i];
    }
    cout << res;
    return 0;
}