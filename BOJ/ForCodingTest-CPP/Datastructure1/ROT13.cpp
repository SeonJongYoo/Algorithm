// ROT13

#include <iostream>
#include <string>
using namespace std;


int main() {
    string s;
    getline(cin, s);
    char tmp;
    for (int i = 0; i < s.length(); i++) {
        if (64 < s[i] && s[i] < 91) {
            tmp = ((int)s[i]%65 + 13)%26 + 65;
            cout << tmp;
        } else if(96 < s[i] && s[i] < 123) {
            tmp = ((int)s[i]%97 + 13)%26 + 97;
            cout << tmp;
        } else {
            cout << s[i];
        }
    }
    
    return 0;
}