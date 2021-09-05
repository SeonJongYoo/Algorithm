// 합분해

#include <iostream>
using namespace std;

const int MAX = 201;
const long long d = 1000000000;
long long dp[MAX][MAX];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, k;
    cin >> n >> k;
    // dp[x][y] : 숫자 x개를 사용해서 y를 만드는 경우의 수
    for (int i = 0; i < n+1; i++) dp[1][i] = 1; // 숫자 1개 사용
    for (int i = 1; i < k+1; i++) dp[i][0] = 1; // 0을 만드는 경우
    if (k == 1) cout << 1;
    else {
        for (int i = 1; i < n+1; i++) {
            for (int j = 2; j < k+1; j++) {
                for (int x = i; x > -1; x--) {
                    dp[j][i] += (dp[j-1][x] % d);
                }
            }
        }
        cout << dp[k][n]%d;
    }

    return 0;
}