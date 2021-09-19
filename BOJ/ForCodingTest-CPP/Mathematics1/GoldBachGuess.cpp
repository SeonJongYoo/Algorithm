// 골드바흐의 추측

#include <iostream>
using namespace std;

const int MAX = 1000001;
long long num[MAX] = {0, };

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    for (long long i = 2; i < MAX; i++) {
        if (num[i] == 0) {
            for (long long j = i*i; j < MAX; j += i) {
                num[j] = 1;
            }
        }
    }
    while (1) {
        int n;
        cin >> n;
        if (!n) break;
        for (int i = 2; i < n+1; i++) {
            if (num[i] == 0 && num[n-i] == 0) {
                cout << n << " = " << i << " + " << n-i << "\n";
                break;
            } 
        }
    }

    
    return 0;
}