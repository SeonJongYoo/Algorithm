/*#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N; int n;
	cin >> N;
	
	vector<int> input;
	for (int i = 0; i < N; i++) {
		cin >> n;
		input.push_back(n);
	}
	int count = 0;
	for (int i = 0; i < input.size(); i++)
	{
		//���� ���� ����
		if (count % 3 == 0 && input[i] == 0) {
			count++;
		}
		//���� ���� ����
		if (count % 3 == 1 && input[i] == 1) {
			count++;
		}
		//�ٳ��� ���� ����
		if (count % 3 == 2 && input[i] == 2) {
			count++;
		}
	}
	cout << count;
	return 0;
}*/