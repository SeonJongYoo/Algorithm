// 숨바꼭질 6

#include <iostream>
using namespace std;

const int MAX = 100001;
int A[MAX] = {0, };

int GCD(int x, int y) {
    int tmp;
    while (y != 0) {
        tmp = x;
        x = y;
        y = tmp % y;
    }
    return x;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n, s;
    cin >> n >> s;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        A[i] = abs(s-a);
    }
    int res = A[0];
    if (n > 1) {
        for (int i = 1; i < n; i++) {
            res = GCD(res, A[i]);
        }
    }
    cout << res;
    
    return 0;
}