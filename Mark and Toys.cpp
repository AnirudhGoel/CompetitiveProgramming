#include <iostream>
#include <cstdlib>
#include <climits>
using namespace std;

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int main() {
	int N, K, A[100000],i = 0,total = 0,ans = 0;
	cin>>N>>K;
	for(i=0;i<N;i++)
	{
		cin>>A[i];
	}
	qsort(A,N,sizeof(int),compare);
	while total < K
	{
		total = total + A[i]
		i++;
		ans++;
	}
	cout<<ans;
	return 0;
}