#include <iostream>
using namespace std;

int main() {
	int N;
	cin >> N;
	
	int K[1000]={0};
	int i=0;
	for(int x=0;x<1667;x++) {
		for(int y=0;3*x+5*y<=N;y++) {
			if(N==3*x+5*y) {
				K[i]=x+y;
				i++;
			}
		}
	}
	if(K[0]==0) {
		cout << -1 << endl;
	} else {
		cout << K[0] << endl;
	}
	return 0;
}
