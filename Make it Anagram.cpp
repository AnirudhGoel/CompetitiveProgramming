#include <iostream>
#include <string>
using namespace std;

int main()
{
	string a,b;
	int i,c[26],d[26],p=0;
	cin>>a;
	cin>>b;
	for(i=0;i<26;i++)
	{
		c[i] = 0;
		d[i] = 0;
	}
	for(i=0;a[i] != '\0';i++)
	{
		c[(int)a[i] - 97] ++;
	}
	for(i=0;b[i] != '\0';i++)
	{
		d[(int)b[i] - 97] ++;
	}
	for(i=0;i<26;i++)
	{
		p = p + abs(c[i] - d[i]);
	}
	cout<<p;
}