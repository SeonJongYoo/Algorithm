// 가장 긴 감소하는 부분 수열

#include <iostream>
using namespace std;

const int MAX = 1001;
int A[MAX];
int dp[3][MAX];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    for (int i = 1; i < n+1; i++) cin >> A[i];

    dp[0][1] = 1;
    dp[1][n] = 1;
    int res = 1;
    if (n > 1) {
        for (int i = 2; i < n+1; i++) {
            int tmp = A[i];
            for (int j = i-1; j > 0; j--) {
                if (tmp > A[j]) {
                    if (dp[0][j] + 1 > dp[0][i]) dp[0][i] = dp[0][j] + 1;
                } else if (dp[0][i] == 0) dp[0][i] = 1;
            }
        }

        for (int i = n-1; i > 0; i--) {
            int tmp = A[i];
            for (int j = i+1; j < n+1; j++) {
                if (tmp > A[j]) {
                    if (dp[1][j] + 1 > dp[1][i]) dp[1][i] = dp[1][j] + 1;
                } else if (dp[1][i] == 0) dp[1][i] = 1;
            }
        }

        for (int i = 1; i < n+1; i++) {
            int tmp = A[i];
            for (int j = i+1; j < n+1; j++) {
                if (tmp > A[j]) {
                    if (dp[2][i] < dp[0][i] + dp[1][j]) dp[2][i] = dp[0][i] + dp[1][j];
                } else if (dp[2][i] == 0) {
                    if (dp[0][i] > dp[1][i]) dp[2][i] = dp[0][i];
                    else dp[2][i] = dp[1][i];
                }
            }
        }
        if (dp[0][n] > dp[1][n]) dp[2][n] = dp[0][n];
        else dp[2][n] = dp[1][n];

        for (int i = 1; i < n+1; i++) {
            if (res < dp[2][i]) res = dp[2][i];
        }
    }
    cout << res;
    
    

    return 0;
}