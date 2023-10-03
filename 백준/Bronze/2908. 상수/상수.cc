#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
string a, b;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    cin >> a >> b;
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    cout << max(a, b);

    return 0;
}