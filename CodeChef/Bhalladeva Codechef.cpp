#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int N, Q, K;
	long int total=0, m, n;
	cin>>N;
	int A[N] = {0};
	for (int i = 1; i <= N; i++)
	{
		cin>>A[i];
	}
	sort(A, A+N+1);
	cin>>Q;
	for (int i = 1; i <= Q; i++)
	{
		m = 0;
		n = N + 1;
		total = 0;
		cin>>K;
		while(m < n-1)
		{
			m++;
			total += A[m];
			n = n - K;
		}
		cout<<total<<endl;
	}
	return 0;
}