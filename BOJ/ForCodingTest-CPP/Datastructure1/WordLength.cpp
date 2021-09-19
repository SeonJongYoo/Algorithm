// 문자열 길이

#include <iostream>
using namespace std;

char word[101] = {0, };

int main() {
    cin >> word;
    int l = 0;
    for (int i = 0; i < 101; i++) {
        if (word[i] == '\0') break;
        l++;
    }
    cout << l;
    return 0;
}