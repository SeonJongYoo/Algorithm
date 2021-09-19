// 추석 트래픽

//  부동소수점 사칙연산에서 문제 발생
// #include <iostream>
// #include <string>
// #include <vector>
// #include <sstream>
// #include <cmath>
// #include <algorithm>

// using namespace std;

// int solution(vector<string> lines) {
//     int answer = 0;
//     vector<float> time;
//     for (int i = 0; i < lines.size(); i++) {
//         istringstream ss(lines[i]);
//         string buf;
//         vector<string> tmp;
//         while (getline(ss, buf, ' ')) {
//             tmp.push_back(buf);
//         }
//         istringstream ss1(tmp[1]); // 초 파싱
//         string buf1;
//         vector<string> tmp1;
//         while (getline(ss1, buf1, ':')) {
//             tmp1.push_back(buf1);
//         }
//         float en = stof(tmp1[2]);
//         float st = en - stof(tmp[2]) + (float)0.001;
//         if (st < (float)0.0) {
//             st = (float)60.0 + st;
//             en = (float)60.0 + en;
//         }
//         time.push_back(st);
//         time.push_back(en);
//     }
//     for (int i = 0; i < time.size(); i++)
//         cout << time[i] << ' ';
//     cout << '\n';

//     float start = time[0];
//     int res = 0;
//     while (start <= time.back()) { // 구간에 포함되는 로그 찾기
//         int cnt = 0;
//         for (int i = 0; i < time.size(); i+=2) {
//             if (start > time[i+1] || start + (float)0.999 < time[i]) continue;
//             cnt++;
//         }
//         res = max(res, cnt);
//         float tmp = start * 1000 + 1.0F;
//         int x = tmp;
//         if (tmp - x >= 0.001f) {
//             x++;
//         }
//         start = (float)x / 1000;
//     }
//     answer = res;
//     return answer;
// }


// 정답 코드
// '초'의 경우 소수점을 기준으로 파싱하여 처리
// 57.021 -> 57과 0.021로 파싱하여 stod()를 적용한다. 
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int solution(vector<string> lines) {
    int answer = 0;
    vector<double> time;
    for (int i = 0; i < lines.size(); i++) {
        istringstream ss(lines[i]);
        string buf;
        vector<string> tmp;
        while (getline(ss, buf, ' ')) {
            tmp.push_back(buf);
        }
        istringstream ss1(tmp[1]); // 초 파싱
        string buf1;
        vector<string> tmp1;
        while (getline(ss1, buf1, ':')) {
            tmp1.push_back(buf1);
        }
        double en = stod(tmp1[0]) * 3600 + stod(tmp1[1]) * 60 + stod(tmp1[2].substr(0, 2)) + stod(tmp1[2].substr(3, 6))/1000.0;
        double st = en - stod(tmp[2]) + 0.001;
        time.push_back(st);
        time.push_back(en);
    }

    // 비교하기
    // lines 배열은 응답'완료'시간을 기준으로 오름차순 정렬됨!!!
    // => 따라서, 다음 로그의 응답 완료 시간이 항상 현재 로그의 응답 완료 시간과 "같거나 크다는 것이 보장"된다!!!
    int res = 0;
    for (int i = 0; i < time.size(); i+=2) {
        //double start = time[i];
        double end = time[i+1];
        int cnt = 1; // i번째 요청은 무조건 포함하므로 1로 초기화!
        for (int j = i+2; j < time.size(); j+=2) {  // 다음 로그부터 모든 로그를 돌면서 처리가 가능한지 확인
            if (end + 1 > time[j]) cnt++;  // end+1 == time[j]가 아닌 이유: 시작 시간과 끝나는 시간을 포함한다는 조건!
        }
        res = max(res, cnt);
    }
    answer = res;
    return answer;
}

int main(void) {
    vector<string> s;
    s.push_back("2016-09-15 00:00:00.000 2.3s");
    s.push_back("2016-09-15 23:59:59.999 0.1s");
    int res = solution(s);
    cout << res << '\n';
}