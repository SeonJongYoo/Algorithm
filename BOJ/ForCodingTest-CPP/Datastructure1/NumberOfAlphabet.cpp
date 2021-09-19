// 알파벳 개수

#include <iostream>
#include <stack>
using namespace std;

const int MAX = 101;
char S[MAX];
int alpha[27];

int main() {
    cin >> S;
    for (int i = 0; i < MAX; i++) {
        if (S[i] == '\0') break;
        alpha[(int)S[i] - 97]++;
    }
    for (int i = 0; i < 26; i++) {
        cout << alpha[i] << " ";
    }
    
    return 0;
}