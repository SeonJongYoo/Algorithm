// 오등큰수

#include <iostream>
#include <cstring>
#include <stack>
using namespace std;

const int MAX = 1000001;
int seq[MAX];
int FA[MAX];

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> seq[i];
    for (int i = 0; i < n; i++) FA[seq[i]-1]++;

    int *res = new int[n];
    memset(res, -1, sizeof(int)*n);

    stack<int> s;
    s.push(0);
    int i = 1;
    while (!s.empty() && i < n) {
        while (!s.empty() && FA[seq[s.top()]-1] < FA[seq[i]-1]) {
            res[s.top()] = seq[i];
            s.pop();
        }
        s.push(i);
        i++;
    }
    for (int i = 0; i < n; i++) cout << res[i] << " ";

    return 0;
}