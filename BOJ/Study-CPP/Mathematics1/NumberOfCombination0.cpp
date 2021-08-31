// 조합 0의 개수

#include <iostream>
using namespace std;


pair<long long, long long> ZeroInFac(int N) {
    pair<long long, long long> p;
    long long two = 0, five = 0;
    long long n2 = 2, n5 = 5;
    // 이 부분이 핵심!!
    // N을 n2로 나눈 몫이 의미하는 바 - 1 ~ N까지 n2를 인수로 가지는 숫자의 개수 -> N!을 소인수분해 했을 때 2의 개수!
    while (n2 <= N) {
        two += N / n2;
        n2 *= 2;
    }
    // N을 n5로 나눈 몫이 의미하는 바 - N!을 소인수분해 했을 때 5의 개수!
    while (n5 <= N) {
        five += N / n5;
        n5 *= 5;
    }
    p.first = two; p.second = five;
    return p;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    pair<long long, long long> ja;
    pair<long long, long long> mo1;
    pair<long long, long long> mo2;
    int n, m;
    cin >> n >> m;
    ja = ZeroInFac(n);
    mo1 = ZeroInFac(n-m);
    mo2 = ZeroInFac(m);

    long long r1 = 0, r2 = 0;
    r1 = ja.first - (mo1.first + mo2.first);
    r2 = ja.second - (mo1.second + mo2.second);

    if (r1 >= r2) cout << r2;
    else cout << r1; 
    
    
    return 0;
}