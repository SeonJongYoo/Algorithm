// 최대 공약수와 최소 공배수

#include <iostream>
using namespace std;

int main() {
    int a, b, tmp, x, y;
    cin >> a >> b;
    x = a; y = b;
    while (b != 0) {
        tmp = a;
        a = b;
        b = tmp % b;
    }
    cout << a << "\n";
    cout << a * (x / a) * (y / a);
    return 0;
}