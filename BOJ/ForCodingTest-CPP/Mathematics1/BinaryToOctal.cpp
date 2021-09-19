// 2진수 8진수

#include <iostream>
#include <cmath>
#include <string>
using namespace std;

void toOct(string s) {
    int n = 0;
    int k = 2;
    for (int i = 0; i < s.length(); i++) {
        n += (int)pow(2, k) * (s[i]-'0');
        k--;
    }
    cout << n;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    string num;
    cin >> num;
    if (num.length() % 3) {
        while (num.length()%3) num = '0' + num;
    }
    for (int i = 0; i < num.length() ; i+=3) {
        toOct(num.substr(i, 3));
    }    
    return 0;
}