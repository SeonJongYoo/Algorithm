// 네 수


#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b, c, d;
    cin >> a >> b >> c >> d;
    long long sum = stoll(a+b) + stoll(c+d);
    cout << sum;

    return 0;
}