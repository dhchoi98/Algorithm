#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
string s;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
     
    int words = 1;
    getline(cin, s);

    int n = s.length(); 
 
    if(n == 0 || n == 1 && s == " "){
        words = 0;
    }
    else{
        for(int i = 0; i < n; i++){
        if(s[i] == ' ')
            words++;
        }
        if(s[0] == ' '){
            words--;  
        }
        if(s[n - 1] == ' '){
            words--;
        }
    } 
    
    cout << words;

    return 0;
}