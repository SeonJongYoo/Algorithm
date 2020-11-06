#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N;
	cin >> N;

	vector<char> input;
	vector<int> input_cnt(N);
	for (int i = 0; i < N; i++) {
		char seat;
		cin >> seat;
		input.push_back(seat);
	}

	if (N == 1 && input[0] == 'S') {
		int count = 1;
		cout << count << "\n";
	}
	else {
		int count = 0; int couple = 0; 
		for (int i = 0; i < input.size(); i++) {
			if (input[i] == 'S') {
				input_cnt[i] = 1;
			}
			else {
				couple++;
				if (couple == 2) {
					if (i == input.size() - 1) {
						input_cnt[i] = 1;
					}
					else {
						//현재 위치에서 끝까지 L이 나오면 현재 L은 컵홀더를 쓸 수 없음!
						bool flag = false;
						for (int j = i + 1; j < input.size(); j++) {
							if (input[j] == 'L') {
								flag = true;
							}
						}
						if (flag == true) {
							couple = 0;
						}
						else {
							input_cnt[i] = 1;
						}
					}
				}
				else {
					input_cnt[i] = 1;
				}
			}
			count += input_cnt[i];
		}
		cout << count << "\n";
	}
	
	return 0;
}