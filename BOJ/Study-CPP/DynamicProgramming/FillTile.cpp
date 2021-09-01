// 가장 긴 감소하는 부분 수열

// 오답
// #include <iostream>
// using namespace std;

// const int MAX = 31;
// int dp[3][MAX];

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(NULL);
//     cout.tie(NULL);

//     int n;
//     cin >> n;

//     if (n > 1) {
//         dp[0][2] = 1;
//         dp[1][2] = 1;
//         dp[2][2] = 1;
//         dp[0][4] = 4;
//         dp[1][4] = 4;
//         dp[2][4] = 3;
//         for (int i = 6; i < n+1; i++) {
//             if (i%2 == 1) continue;
//             dp[0][i] = dp[0][i-2] + dp[1][i-2] + dp[2][i-2] + 3;
//             dp[1][i] = dp[0][i-2] + dp[1][i-2] + dp[2][i-2] + 3;
//             dp[2][i] = dp[0][i-2] + dp[1][i-2] + dp[2][i-2];
//         }
//     }
//     cout << dp[0][n] + dp[1][n] + dp[2][n];

//     return 0;
// }


#include <iostream>
using namespace std;

const int MAX = 31;
int dp[MAX];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    dp[0] = 1;
    dp[2] = 3;
    for (int i = 4; i < n+1; i++) {
        dp[i] = dp[i-2]*3; // 기본 3x2 도형을 오른쪽에 넣는 경우
        for (int j = 4; j < i+1; j+=2) { // 3x2 도형 이외에 n이 4이상일 때, 새로운 형태의 도형이 2개씩 추가
            // j += 2: 2씩 증가하면서 타일이 채워진다.
            dp[i] += dp[i-j]*2;
        }
    }
    cout << dp[n];
    return 0;
}