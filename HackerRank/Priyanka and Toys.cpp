#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

int main()
{
	int num, j;

	vector<int> w;
	cin>>num;
	
	for (int i = 0; i < num; i++) {
		cin>>j;
		w.push_back(j);
	}
	
	sort(w.begin(), w.end());
	int temp = w[0], buy = 1;
	
	for (int i = 0; i < num; i++) {
		if(w[i] - temp > 4) {
			buy++;
			temp = w[i];
		}
	}
	
	cout<<buy;
	return 0;
}
