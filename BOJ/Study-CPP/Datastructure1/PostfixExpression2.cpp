// 후위표기식2

#include <iostream>
#include <stack>
using namespace std;

const int MAX = 101;
char Exp[MAX];
int num[MAX];

int main() {
    int n;
    cin >> n;
    cin >> Exp;
    for (int i = 0; i < n; i++)
        cin >> num[i];

    stack<double> s;
    for (int i = 0; i < MAX; i++) {
        if (Exp[i] == '\0') break;
        if (int(Exp[i]) > 64 && int(Exp[i]) < 91) s.push((double)num[int(Exp[i])-65]);
        else {
            double x1, x2, r;
            x1 = s.top();
            s.pop();
            x2 = s.top();
            s.pop();
            switch(Exp[i]) {
                case '*':
                    r = x1 * x2;
                    break;
                case '/':
                    r = (double)x2 / x1;
                    break;
                case '+':
                    r = x1 + x2;
                    break;
                case '-':
                    r = x2 - x1;
                    break;
            }
            s.push(r);
        }
    }
    cout << fixed;
    cout.precision(2);
    cout << s.top() << endl;
    return 0;
}