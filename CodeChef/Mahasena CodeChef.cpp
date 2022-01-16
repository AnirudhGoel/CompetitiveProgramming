#include <iostream>
using namespace std;

int main() {
	int N, A ,t=0;
	cin>>N;
	for (int i = 0; i < N; ++i)
	{
		cin>>A;
		if (A % 2 == 0)
		{
			t++;
		}
	}
	(t > (N - t)) ? (cout<<"READY FOR BATTLE") : (cout<<"NOT READY");
	return 0;
}