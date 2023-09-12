#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int num;
    int arr[1000000];
    int min, max;
    cin >> num;

    for(int i = 0; i < num; i++){
        cin >> arr[i];
    }
    min = arr[0];
    max = arr[0];
    for(int j = 0; j < num; j++){
        if(arr[j] > max){
            max = arr[j];
        }
        if(arr[j] < min){
            min = arr[j];
        }
    }
    cout << min << " " << max;

    return 0;
}