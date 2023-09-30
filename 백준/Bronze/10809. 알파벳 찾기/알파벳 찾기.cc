#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
string s;
int alpha[26]; 

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    cin >> s;
    
    for(int i = 0; i < 26; i++){
        alpha[i] = s.find(i + 97);  
    }

    for(int i = 0; i < 26; i++){
        cout << alpha[i] << " ";
    }

    return 0;
}