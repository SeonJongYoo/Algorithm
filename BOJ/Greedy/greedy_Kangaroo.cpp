/*#include <iostream>

using namespace std;

//백준은 파일로 입력이 주어지므로 파일 끝에는 항상 EOF가 존재!!!
int main() {
    int a, b, c;
    while (cin >> a >> b >> c) {
        int count_a = 0; int count_c = 0;
        if (b - a > 1) {
            count_c = b - a - 1;
        }

        if (c - b > 1) {
            count_a = c - b - 1;
        }

        if (count_a >= count_c) {
            cout << count_a << endl;
        }
        else {
            cout << count_c << endl;
        }
    }

    return 0;
}*/