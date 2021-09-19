// 연속합 2

// #include <iostream>
// using namespace std;

// const int MAX = 100001;
// int seq[MAX];
// int dp[MAX];

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(NULL);
//     cout.tie(NULL);
    
//     int n;
//     cin >> n;
//     for (int i = 1; i < n+1; i++)
//         cin >> seq[i];
    
//     int max = -1000000000;
//     // 아무것도 지우지 않았을 때
//     dp[1] = seq[1];
//     for (int i = 2; i < n+1; i++) {
//         if (dp[i-1] + seq[i] > seq[i]) dp[i] = dp[i-1] + seq[i];
//         else dp[i] = seq[i];
//     }
//     for (int i = 1; i < n+1; i++) {
//         if (dp[i] > max) max = dp[i];
//     }

//     // 한 개씩 지우는 경우
//     for (int k = 1; k < n+1; k++) {
//         for (int i = 1; i < n+1; i++) {
//             if (i == k) {
//                 dp[i] = dp[i-1];
//             } else {
//                 if (dp[i-1] + seq[i] > seq[i]) dp[i] = dp[i-1] + seq[i];
//                 else dp[i] = seq[i];
//             }
//         }
//         for (int i = 1; i < n+1; i++) {
//             if (dp[i] > max) max = dp[i];
//         }
//     }
//     cout << max;

//     return 0;
// }


// 정답 코드 1 - 2차원 배열 사용
#include <iostream>
using namespace std;

const int MAX = 100001;
int seq[MAX];
int dp[2][MAX];
// dp[0][x]: x번 째 숫자를 지우는 경우
// dp[1][x]: x번 째 숫자를 지우지 않는 경우

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < MAX; j++) {
            dp[i][j] = -1000000001;  // 0으로 초기화하면 숫자를 하나 선택하지 않는 경우가 발생! - 조건 위배
        }
    }

    int n;
    cin >> n;
    for (int i = 1; i < n+1; i++)
        cin >> seq[i];
    
    int max = -1000000000;
    dp[1][1] = seq[1];
    for (int i = 2; i < n+1; i++) {
        // 현재 값을 삭제하지 않고 이전 값을 삭제했을 때와 
        // 현재 값을 삭제했을 때를 비교
        if (dp[0][i-1] + seq[i] > dp[1][i-1]) dp[0][i] = dp[0][i-1] + seq[i]; 
        else dp[0][i] = dp[1][i-1];

        // 현재값을 삭제하지 않는 경우와
        // 현재값만 선택했을 때를 비교
        if (dp[1][i-1] + seq[i] > seq[i]) dp[1][i] = dp[1][i-1] + seq[i];
        else dp[1][i] = seq[i];
    }

    for (int i = 0; i < 2; i++) {
        for (int j = 1; j < n+1; j++) {
            if (dp[i][j] > max) max = dp[i][j];
            //cout << dp[i][j] << " ";
        }
        //cout << endl;
    }
    cout << max;

    return 0;
}


// 정답 코드 2 - 1차원 배열 사용
// 수열에서 특정 위치 i번째 숫자를 제거한 경우 연속합은
// i를 기준으로 i-1번째까지 연속합의 최댓값과 i+1번째까지 연속합의 최댓값을 더하여 구할 수 있다.
// => Left_Sum[i-1] + Right_Sum[i+1] 
// Left_Sum: 수열의 왼쪽에서부터 오른쪽의 순서로 구한 연속합
// Right_Sum: 수열의 오른쪽에서부터 왼쪽의 순서로 구한 연속합 
// #include <iostream>
// using namespace std;

// const int MAX = 100001;
// int seq[MAX];
// int dp1[MAX]; // L -> R
// int dp2[MAX]; // R -> L
// // dp[0][x]: x번 째 숫자를 지우는 경우
// // dp[1][x]: x번 째 숫자를 지우지 않는 경우

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(NULL);
//     cout.tie(NULL);

//     int n;
//     cin >> n;
//     for (int i = 1; i < n+1; i++)
//         cin >> seq[i];

//     int max = seq[1];
    
//     // 왼쪽에서 오른쪽 방향으로 연속합을 구하는 경우
//     dp1[1] = seq[1];

//     for (int i = 2; i < n+1; i++) {
//         if (dp1[i-1] + seq[i] > seq[i]) dp1[i] = dp1[i-1] + seq[i];
//         else dp1[i] = seq[i];

//         if (dp1[i] > max) max = dp1[i];
//     }

//     // 오른쪽에서 왼쪽 방향으로 연속합을 구하는 경우
//     dp2[n] = seq[n];
//     for (int i = n-1; i > -1; i--) {
//         if (dp2[i+1] + seq[i] > seq[i]) dp2[i] = dp2[i+1] + seq[i];
//         else dp2[i] = seq[i];
//     }

//     // i번째 원소를 삭제하는 경우
//     for (int i = 2; i < n; i++) {
//         int tmp = dp1[i-1] + dp2[i+1];
//         if (tmp > max) max = tmp;
//     }
//     cout << max;

//     return 0;
// }