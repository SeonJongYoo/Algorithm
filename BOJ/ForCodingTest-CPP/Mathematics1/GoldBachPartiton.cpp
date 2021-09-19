// 골드바흐 파티션

#include <iostream>
#include <string>
using namespace std;

const int MAX = 1000001;
int num[MAX] = {0, };

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    for (long long x = 2; x < MAX; x++) {
        if (num[x] == 0) {
            for (long long y = x*x; y < MAX; y += x) {
                if (num[y] == 0) num[y] = 1;
            }
        }
    }

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int cnt = 0;
        if (n == 4) cnt = 1;
        else {
            for (int i = 3; i <= n/2; i+=2) {
                if (num[i] == 0 && num[n-i] == 0) {
                    cnt++;
                }
            }
        }
        cout << cnt << "\n";
    }


    return 0;
}