// RGB 거리 2

#include <iostream>
#include <algorithm>
using namespace std;

const int MAX = 1001;
int cost[MAX][4];
int dp[MAX][4];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    for (int i = 1; i < n+1; i++) {
        for (int j = 1; j < 4; j++) {
            cin >> cost[i][j];
        }
    }

    int Min = 1000001;

    // 1번 집에 칠할 색을 고정하고 연산을 진행
    for (int i = 1; i < 4; i++) {
        for (int j = 1; j < 4; j++) {
            if (i == j) dp[1][j] = cost[1][j];
            else dp[1][j] = 1000001;
        }
        for (int j = 2; j < n+1; j++) {
            dp[j][1] = min(dp[j-1][2], dp[j-1][3]) + cost[j][1];
            dp[j][2] = min(dp[j-1][1], dp[j-1][3]) + cost[j][2];
            dp[j][3] = min(dp[j-1][1], dp[j-1][2]) + cost[j][3]; 
        }
        // 연산이 끝나면 바로 최솟값을 구한다.
        // 이때, 1번 집에서 칠한 색깔의 경우는 제외한다.
        for (int j = 1; j < 4; j++) {
            if (i == j) continue;
            if (Min > dp[n][j]) Min = dp[n][j];
        }
    }
    cout << Min;
    return 0;
}