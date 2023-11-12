#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string str;  
int cnt[26]; // 전역변수로 선언 시 0으로 초기화가 된다. 

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> str; 
    for(char a : str){
    	cnt[a - 'a']++;    // 인덱스는 a : 0 , b : 1, c : 2, ,,,, 의 결과를 가지게 된다.
	}
	for(int i = 0; i < 26; i++){ 
		cout << cnt[i] << " ";
	}
	
	return 0; 
}