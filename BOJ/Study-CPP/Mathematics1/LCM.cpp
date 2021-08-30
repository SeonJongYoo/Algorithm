// 최소공배수

#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    int a, b, tmp;
    int x, y;
    cin >> t;
    while (t-- > 0) {
        cin >> a >> b;
        x = a; y = b;
        while (b != 0) {
            tmp = a;
            a = b;
            b = tmp % b;
        }
        cout << a * (x / a) * (y / a) << "\n";
    }
    return 0;
}