#include <iostream>
using namespace std;

int main() {
	int n, q, l, r, type, total = 0;
	cin>>n>>q;
	int arr[n+1] = {0};
	for (int i = 0; i < q; ++i)
	{
		cin>>type;
		cin>>l>>r;
		if (type == 1)
		{
			for (int j = l; j <= r; ++j)
			{
				arr[j]++;
			}
		} else if (type == 2)
		{
			total = 0;
			for (int k = l; k <= r; ++k)
			{
				total += arr[k];
			}
			cout<<total<<endl;
		}
	}
	return 0;
}