#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

string s;


int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    string a, b;
    cin >> s;
    int half = s.length() / 2;
    
    if(s.length() % 2 == 0){ // 짝수 끝날때
        a = s.substr(0, half);
        b = s.substr(half);
    }
    else{
        a = s.substr(0, half);
        b = s.substr(half + 1);
    }
    
    reverse(b.begin(), b.end()); 
  
    if(a == b){
        cout << 1;
    }
    else{
        cout << 0;
    }

    return 0;
}