// 후위표기식

#include <iostream>
#include <stack>
using namespace std;

const int MAX = 101;
char Exp[MAX];

int main() {
    cin >> Exp;
    stack<char> s;
    int i = 0;
    while (Exp[i] != '\0') {
        if (int(Exp[i]) > 64 && int(Exp[i]) < 91) cout << Exp[i];
        else {
            if (Exp[i] == ')') {
                while (s.top() != '(') {
                    cout << s.top();
                    s.pop();
                }
                s.pop();
                i++;
                continue;
            } else if (Exp[i] == '*' || Exp[i] == '/') {
                while(!s.empty() && (s.top() == '*' || s.top() == '/')) {
                    cout << s.top();
                    s.pop();
                }
            // 연산자 우선순위 고려 -> '+' 나 '-'를 스택에 넣으려할 때
            } else if (Exp[i] == '+' || Exp[i] == '-') {
                while (!s.empty() && s.top() != '(') {
                    cout << s.top();
                    s.pop();
                }
            }
            s.push(Exp[i]);
        }
        i++;
    }
    while (!s.empty()) {
        cout << s.top();
        s.pop();
    }
    return 0;
}