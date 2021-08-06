// // 문자열 분석

// #include <iostream>
// #include <string>
// using namespace std;

// int main() {
//     string S;
//     // getline: 엔터("\n")를 무시하고 계속 입력을 받다가 파일 종료 조건을 입력 받으면 입력을 멈춤
//     while (getline(cin, S)) {
//         int r1 = 0; int r2 = 0; int r3 = 0; int r4 = 0;
//         for (int i = 0; i < S.length(); i++) {
//             if ((int)S[i] > 96 && (int)S[i] < 123)
//                 r1++;
//             else if ((int)S[i] > 64 && (int)S[i] < 91) 
//                 r2++;
//             else if (S[i] == ' ')
//                 r4++;
//             else
//                 r3++;
//         }
//         cout << r1 << " " << r2 << " " << r3 << " " << r4 << "\n";
//     }
//     return 0;
// }


// char 배열 사용
#include <iostream>
#include <string>
using namespace std;

int main() {
    char S[101];
    // getline: 엔터("\n")를 무시하고 계속 입력을 받다가 파일 종료 조건을 입력 받으면 입력을 멈춤
    while (1) {
        cin.ignore();
        cin.getline(S, 101);
        int r1 = 0; int r2 = 0; int r3 = 0; int r4 = 0;
        for (int i = 0; i < 101; i++) {
            if (S[i] == '\n') break;
            if ((int)S[i] > 96 && (int)S[i] < 123)
                r1++;
            else if ((int)S[i] > 64 && (int)S[i] < 91) 
                r2++;
            else if (S[i] == ' ')
                r4++;
            else
                r3++;
        }
        cout << r1 << " " << r2 << " " << r3 << " " << r4 << "\n";
    }
    return 0;
}