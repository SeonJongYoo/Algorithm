// -2진수

#include <iostream>
using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int num;
    cin >> num;
    int i = 0;
    int tmp = -num;
    while (tmp) {
        if (i % 2 == 0) {
            cout << tmp % 2 << endl;
            tmp /= -2;
        } else {
            cout << tmp % -2 << endl;
            tmp /= -2;
        }
        i++;
    }

    return 0;
}