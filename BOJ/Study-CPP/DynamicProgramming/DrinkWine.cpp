// 포도주 시식

#include <iostream>
using namespace std;

const int MAX = 10001;
int wine[MAX];
int dp[MAX];


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    for (int i = 1; i < n+1; i++)
        cin >> wine[i];
    dp[1] = wine[1];
    if (n > 1) {
        dp[2] = wine[2] + wine[1];
        for (int i = 3; i < n+1; i++) {
            int Max = 0;
            // 3잔 연속 마실 수 없다는 조건!
            if (wine[i] + dp[i-2] > Max) Max = wine[i] + dp[i-2];
            if (wine[i] + wine[i-1] + dp[i-3] > Max) Max = wine[i] + wine[i-1] + dp[i-3];
            if (dp[i-1] > Max) Max = dp[i-1];
            dp[i] = Max;
        }
    }
    cout << dp[n];

    return 0;
}