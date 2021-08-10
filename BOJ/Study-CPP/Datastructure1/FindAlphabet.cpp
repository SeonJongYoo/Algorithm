// 알파벳 찾기

#include <iostream>
using namespace std;

const int MAX = 101;
char S[MAX];

int main() {
    cin >> S;
    int alpha[27];
    for (int i = 0; i < 27; i++) alpha[i] = -1;
    for (int i = 0; i < MAX; i++) {
        if (S[i] == '\0') break;
        if (alpha[(int)S[i]-97] != -1) continue;
        alpha[(int)S[i] - 97] = i;
    }
    for (int i = 0; i < 26; i++) {
        cout << alpha[i] << " ";
    }
    
    return 0;
}