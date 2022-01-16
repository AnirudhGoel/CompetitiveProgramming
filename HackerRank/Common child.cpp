#include <bits/stdc++.h>

using namespace std;

int commonChild(string s1, string s2){
    int len1, len2;

    // Dynamically generating large size 2D array
    int** res = new int*[5001];
    for(int i = 0; i < 5001; ++i)
       res[i] = new int[5001];
    
    len1 = s1.length();
    len2 = s2.length();

    for(int i=0; i<=len1; i++) {
        for(int j=0; j<=len2; j++) {
            res[i][j] = 0;
        }
    }
    for(int i=1; i<=len1; i++) {
        for(int j=1; j<=len2; j++) {
            if(s1[i-1] == s2[j-1])
                res[i][j] = res[i-1][j-1] + 1;
            else
                res[i][j] = max(res[i-1][j], res[i][j-1]);
        }
    }
    
    return res[len1][len2];
}

int main() {
    string s1;
    cin >> s1;
    string s2;
    cin >> s2;
    int result = commonChild(s1, s2);
    cout << result << endl;
    return 0;
}

