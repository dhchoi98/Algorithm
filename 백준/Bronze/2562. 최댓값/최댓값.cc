#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int num[9];
    int seq, max;

    for(int i = 0; i < 9; i++){
        cin >> num[i];
    }
    max = -1;

    for(int j = 0; j < 9; j++){
        if(max < num[j]){
            max = num[j];
            seq = j;
        }
    }

    cout << max << "\n" << seq + 1;

    return 0;
}