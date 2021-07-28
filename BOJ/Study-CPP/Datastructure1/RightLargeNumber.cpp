// 오큰수

// 시간초과
// #include <iostream>
// #include <stack>
// using namespace std;

// const int MAX = 1000001;
// int seq[MAX] = {0, };
// int main() {
//     int n;
//     cin >> n;
//     for (int i = 0; i < n; i++)
//         cin >> seq[i];
//     stack<int> s;
//     stack<int> res;
//     for (int i = 0 ; i < n; i++) {
//         s.push(seq[i]);
//     }
//     int k = 1;
//     while (!s.empty()) {
//         bool flag = false;
//         int tmp = s.top();
//         s.pop();
//         for (int i = n-k; i < n; i++) {
//             if (tmp < seq[i]) {
//                 res.push(seq[i]);
//                 flag = true;
//                 break;
//             }
//         }
//         if (!flag) res.push(-1);
//         k++;
//     }
//     while (!res.empty()) {
//         cout << res.top() << " ";
//         res.pop();
//     }


//     return 0;
// }


// 정답 코드
#include <iostream>
#include <stack>
using namespace std;

const int MAX = 1000001;
int seq[MAX] = {0, };

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> seq[i];

    stack<int> s;
    int *res = new int[n];
    for (int i = 0; i < n; i++) res[i] = -1;

    // 현재보다 큰 숫자를 만나면 res 배열에 저장하고 stack에서 현재의 인덱스를 pop!
    // 현재보다 작은 숫자를 만나면 바로 다음 인덱스를 push하여 연산 진행
    s.push(0);  // 0번째 인덱스부터 stack에 넣어 비교 시작
    int i = 1;
    while (!s.empty() && i < n) {
        while (!s.empty() && seq[s.top()] < seq[i]) {  // 조건을 만족한 숫자의 인덱스는 스택에서 pop!
            res[s.top()] = seq[i];
            s.pop();
        }
        s.push(i);
        i++;
    }

    for (int k = 0; k < n; k++) {
        cout << res[k] << " ";
    }
    
    return 0;
}