#include <iostream>
#include <ctype.h>
#include <string>
using namespace std;

int main() {
	int t, sum=0;
	cin>>t;
	for (int i = 0; i < t; i++)
	{
		sum = 0;
		string str;
		cin>>str;
		for (int i = 0; i < str.size(); i++)
		{
			if (isdigit(str[i])) {
				int ia = str[i] - '0';
				sum += ia;
			}
		}
		cout<<sum<<endl;
	}
	return 0;
}