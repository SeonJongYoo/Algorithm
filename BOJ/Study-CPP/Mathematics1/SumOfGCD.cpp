// GCD 합

#include <iostream>
using namespace std;

const int MAX = 101;
int num[MAX] = {0, };
int visit[MAX] = {0, };
long long res = 0;

int GCD(int x, int y) {
    int tmp;
    while (y != 0) {
        tmp = x;
        x = y;
        y = tmp % y;
    }
    return x;
}

void DFS(int L, int s, int m, int N) {
    if (L == m) {
        int a = 0, b = 0;
        for (int i = 0; i < N; i++) {
            if (visit[i] == 1) {
                if (!a) a = num[i];
                else b = num[i];
            }
        }
        int r = GCD(a, b);
        res += r;
    } else {
        for (int i = s; i < N; i++) {
            if (visit[i] == 0) {
                visit[i] = 1;
                DFS(L+1, i+1, m, N);
                visit[i] = 0;
            }
        }
    }
}

int main() {
    int t = 0;
    cin >> t;
    while (t--) {
        int n = 0;
        cin >> n;
        for (int i = 0; i < n; i++)
            cin >> num[i];
        DFS(0, 0, 2, n);
        cout << res << "\n";
        res = 0;
    }
    
    return 0;
}