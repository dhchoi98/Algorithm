#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int n;
    cin >> n;

    for(int i = 1; i <= n; i++){
        printf("%d", i);
        printf("\n");
    }
    return 0;
}