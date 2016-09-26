#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int N;
	cin>>N;
	for (int i = 0; i < N; i++)
	{
		int K, sum = 0;
		int kid[100] = {0};
		int pen[100] = {0};
		cin>>K;
		for (int i = 0; i < K; i++)
		{
			cin>>kid[i];
		}
		for (int i = 0; i < K; i++)
		{
			cin>>pen[i];
		}
		sort(kid, kid + K);
		sort(pen, pen + K);
		for (int i = 0; i < K; i++)
		{
			sum += abs(kid[i] - pen[i]);
		}
		cout<<sum<<endl;
	}
	return 0;
}