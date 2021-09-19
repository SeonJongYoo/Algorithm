// 팩토리얼 0의 개수

#include <iostream>
using namespace std;

const int MAX = 501;
int num[2][MAX] = {0,};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    if (n > 1) {
        int i = 2;
        while (i < n+1) {
            int tmp1 = i, tmp2 = i;
            while (tmp1 % 2 == 0) {
                tmp1 /= 2;
                num[0][i]++;
            }
            num[0][i] += num[0][i-1];
            while (tmp2 % 5 == 0) {
                tmp2 /= 5;
                num[1][i]++;
            }
            num[1][i] += num[1][i-1];
            i++;
        }
    }
    if (num[0][n] >= num[1][n]) cout << num[1][n];
    else cout << num[0][n];
    
    return 0;
}