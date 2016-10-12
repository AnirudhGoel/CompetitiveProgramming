#include <iostream>
#include <set>
#include <cstring>
using namespace std;

int main() {
	int m, n, count = 0;
	cin>>m>>n;
	string a[m], b[n], c;
	for (int i = 0; i < m; ++i)
	{
		cin>>a[i];
	}
	for (int i = 0; i < n; ++i)
	{
		cin>>b[i];
	}
	for (int i = 0; i < m; ++i)
	{
		for (int j = 0; j < n; ++j)
		{
			set<char> g;
			c = a[i] + b[j];
			for (int k = 0; k < c.size(); ++k)
				g.insert(c[k]);
			count+=(g.size()==26 ? 1: 0);
		}
	}
	cout<<count;
	return 0;
}