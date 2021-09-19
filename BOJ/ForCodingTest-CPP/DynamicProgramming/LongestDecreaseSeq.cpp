// 가장 긴 감소하는 부분 수열

#include <iostream>
using namespace std;

const int MAX = 1001;
int A[MAX];
int dp[MAX];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    for (int i = 1; i < n+1; i++) cin >> A[i];

    dp[1] = 1;
    if (n > 1) {
        for (int i = 2; i < n+1; i++) {
            int tmp = A[i];
            for (int j = i-1; j > 0; j--) {
                if (tmp < A[j]) {
                    if (dp[j] + 1 > dp[i]) dp[i] = dp[j] + 1;
                } else {
                    if (dp[i] == 0) dp[i] = 1;
                }
            }
        }
        int res = 0;
        for (int i = 1; i < n+1; i++) {
            if (res < dp[i]) res = dp[i];
        }
        cout << res;
    } else {
        cout << 1;
    }
    
    

    return 0;
}