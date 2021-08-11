// 팩토리얼

#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    int res = 1;
    cin >> n;
    if (n > 0) {
        while (n != 1) {
            res *= n--;
        }
    }
    cout << res;

    
    return 0;
}