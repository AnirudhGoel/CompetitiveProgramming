#include <iostream>
#include <string>
using namespace std;

int main() {
	string A;
    int i, odd=0, N, B[26];
	cin>>A;
	N = A.length();
	for(i = 0; i < 26; i++)
		B[i] = 0;
	for(i = 0; i < N; i++)
		B[(int) A[i] - 97]++;
	for(i = 0; i < 26; i++)
	{
		if(B[i] % 2 == 1)
		{
			odd++;
		}
		if(odd > 1)
		{
			cout<<"NO";
			break;
		}
	}
	if(odd < 2)
		cout<<"YES";
	return 0;
}