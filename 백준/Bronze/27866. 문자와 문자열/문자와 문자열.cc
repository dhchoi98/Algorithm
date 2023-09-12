#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    string word;
    int num;
    
    cin >> word >> num;
    cout << word[num - 1];

    return 0;
}