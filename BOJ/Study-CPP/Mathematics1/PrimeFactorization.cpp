// 소인수분해

#include <iostream>
#include <string>
using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    if (n > 1) {
        int tmp = n;
        int k = 2;
        while (tmp != 1) {
            while (tmp % k == 0) {
                tmp /= k;
                cout << k << endl;
            }
            k++;
        }
    }


    return 0;
}

// #include <iostream>
// #include <string>
// using namespace std;


// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(NULL);
//     cout.tie(NULL);

//     int n;
//     cin >> n;
//     if (n > 1) {
//         int tmp = n;
//         int k = 2;
//         while (tmp != 1) {
//             if (tmp % k == 0) {
//                 tmp /= k;
//                 cout << k << endl;
//             } else k++;
//         }
//     }


//     return 0;
// }