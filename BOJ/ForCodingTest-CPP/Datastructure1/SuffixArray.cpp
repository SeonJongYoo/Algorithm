// 접미사 배열

#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    string s;
    cin >> s;
    string arr[s.length()];
    for (int i = 0; i < s.length(); i++) {
        arr[i] = s.substr(i);
    }
    sort(arr, arr+s.length());
    for (int i = 0; i < s.length(); i++)
        cout << arr[i] << "\n";

    return 0;
}