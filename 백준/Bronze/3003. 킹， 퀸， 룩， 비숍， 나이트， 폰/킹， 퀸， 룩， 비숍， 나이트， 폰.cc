#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int chess[6] = {1, 1, 2, 2, 2, 8};
int white[6];
int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    for(int i = 0; i < 6; i++){
        cin >> white[i];
    }
    for(int j = 0; j < 6; j++){
        cout << chess[j] - white[j] << " ";  
    }

    return 0;
}