// 불 !
#include <iostream>
#include <string>
#include <queue>
#include <cstring>
#include <algorithm>
#include <climits>
using namespace std;

int r, c;
string board[1002];
queue<pair<int, int>> jh;
queue<pair<int, int>> fire;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int visit1[1002][1002];
int visit2[1002][1002];

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    memset(visit1, -1, sizeof(visit1));
    memset(visit2, -1, sizeof(visit2));

    string s;
    queue<pair<int, int>> escape;
    cin >> r >> c;
    for (int i = 0; i < r; i++) {
        cin >> board[i];
        for (int j = 0; j < c; j++) {
            if (board[i][j] == 'J') {
                jh.push({i, j});
                visit1[i][j] = 0;
                if (i == 0 || i == r-1 || j == 0 || j == c-1) escape.push({i, j});
            }
            else if (board[i][j] == 'F') {
                fire.push({i, j});
                visit2[i][j] = 0;
            }
        }
    }
    while (!jh.empty()) {
        pair<int, int> tmp = jh.front(); jh.pop();
        for (int k = 0; k < 4; k++) {
            int xx = tmp.first + dx[k];
            int yy = tmp.second + dy[k];
            if (xx < 0 || xx >= r || yy < 0 || yy >= c || visit1[xx][yy] != -1) continue;
            if (board[xx][yy] == '#' || board[xx][yy] == 'F') continue;
            if (xx == 0 || xx == r-1 || yy == 0 || yy == c-1) escape.push({xx, yy});
            visit1[xx][yy] = visit1[tmp.first][tmp.second] + 1;
            jh.push({xx, yy});
        }
    }

    while (!fire.empty()) {
        pair<int, int> tmp = fire.front(); fire.pop();
        for (int k = 0; k < 4; k++) {
            int xx = tmp.first + dx[k];
            int yy = tmp.second + dy[k];
            if (xx < 0 || xx >= r || yy < 0 || yy >= c || visit2[xx][yy] != -1) continue;
            if (board[xx][yy] == '#') continue;
            visit2[xx][yy] = visit2[tmp.first][tmp.second] + 1;
            fire.push({xx, yy});
        }
    }

    int res = INT_MAX;
    while (!escape.empty()) {
        pair<int, int> tmp = escape.front(); escape.pop();
        if (visit2[tmp.first][tmp.second] == -1 || visit1[tmp.first][tmp.second] < visit2[tmp.first][tmp.second]) {
            res = min(res, visit1[tmp.first][tmp.second]);
        }
    }
    if (res != INT_MAX) cout << res + 1;
    else cout << "IMPOSSIBLE";
}