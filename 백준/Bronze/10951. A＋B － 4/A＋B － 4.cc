#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    int a, b;

    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    while(cin >> a >> b){
        cout << a + b << "\n";
    }
    

    return 0;
}