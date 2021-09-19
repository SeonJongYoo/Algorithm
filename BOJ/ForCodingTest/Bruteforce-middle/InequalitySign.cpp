// 부등호

#include <iostream>
using namespace std;

const int MAX = 20;
char sign[MAX];
int visit[10];
int arr[MAX];
string Max = "";
string Min = "";

void getMax(int L, int N) {
    if (!Max.empty()) return;
    if (L == N) {
        for (int i = 0; i < N-1; i++) {
            if ((sign[i] == '<' && arr[i] > arr[i+1]) || (sign[i] == '>' && arr[i] < arr[i+1])) {
                Max.clear();
                return;
            }
            Max += (arr[i] + '0');
        }
        Max += (arr[N-1] + '0');
        cout << Max << endl;
    } else {
        for (int i = 9; i > -1; i--)  {
            if (visit[i] == 0) {
                visit[i] = 1;
                arr[L] = i;
                getMax(L+1, N);
                arr[L] = 0;
                visit[i] = 0;
            }
        }
    }
}

void getMin(int L, int N) {
    if (L == N) {
        for (int i = 0; i < N-1; i++) {
            if ((sign[i] == '<' && arr[i] > arr[i+1]) || (sign[i] == '>' && arr[i] < arr[i+1])) {
                Min.clear();
                return;
            }
            Min += (arr[i] + '0');
        }
        Min += (arr[N-1] + '0');
        cout << Min << endl;
        exit(0);
    } else {
        for (int i = 0; i < 10; i++)  {
            if (visit[i] == 0) {
                visit[i] = 1;
                arr[L] = i;
                getMin(L+1, N);
                arr[L] = 0;
                visit[i] = 0;
            }
        }
    }
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int k;
    cin >> k;
    cin.ignore();
    int idx = 0;
    while (1) {
        char t = cin.get();
        if (t == ' ') continue;
        if (t == '\n') {
            sign[idx] = '\n';
            break;
        }
        sign[idx] = t;
        idx++;
    }
    getMax(0, k+1);
    getMin(0, k+1);

    return 0;
}