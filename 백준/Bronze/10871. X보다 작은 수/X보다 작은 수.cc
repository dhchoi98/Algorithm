#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int arr[100000];
    int n, x;
    cin >> n >> x;

    for(int i = 0; i < n; i++){
        cin >> arr[i]; 
    }
    for(int j = 0; j < n; j++){
        if(arr[j] < x)
            cout << arr[j] << " ";
    }
    return 0;
}