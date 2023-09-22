#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int input, path, res = 1;
    int i = 1;
    // 1 7 19 37 61   
    //  6 12 18 24
    cin >> input;  // zZa
    while(input > res){
        res = res + i * 6;
        i++;
    }
    cout << i; 

    return 0;
}