#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

string s;
int alpha[26]; // 알파뱃 개수만큼 배열 생성

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    cin >> s;  // zZa

    for(int i = 0; i < s.length(); i++){
        // A = 65 , a = 97
        if(s[i] < 97)   // 대문자 일 때
            alpha[s[i] - 65]++; 
        else
            alpha[s[i] - 97]++;    
    }
    int max = 0 , max_index = 0;

    for(int j = 0; j < 26; j++){
        if(max < alpha[j]){
            max = alpha[j];
            max_index = j;
        }
    }
    for(int k = 0; k < 26; k++){
        if(max == alpha[k] && k != max_index){
            cout << "?";
            return 0;
        }
    }

    cout << (char)(max_index + 65);
    

    return 0;
}