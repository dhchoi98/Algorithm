#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    int n;
    cin >> n; // 2n - 1 
    for(int i = 1; i <= n; i++){
        for(int j = n - i; j > 0; j--){
            cout << " ";
        }
        for(int k = 1; k < i * 2; k++){
            cout << "*";
        }
        cout << endl;
    }   
    for(int i = 1; i < n; i++){
        for(int j = 0; j < i; j++){
            cout << " ";
        }
        for(int k = 2 * (n - i) - 1; k > 0; k--){
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}