#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

string player[150];
int cnt[26];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    // 선수의 수 입력 (1 ~ 150 명)
    cin >> n;
    
    // 선수의 성 입력 받기 (명 수대로)
    for(int i = 0; i < n; i++){
        cin >> player[i];
    }
    // 알파벳 별로 선수의 성 개수 저장
    for(int j = 0; j < n; j++){
       cnt[player[j][0] - 'a']++; 
    }
    // 출력
    char alpha;
    int predaja = 0;
    for(int k = 0; k < 26; k++){
        if(cnt[k] >= 5){
            alpha =  97 + k;
            cout << alpha;
            predaja++;
        }
    }
    if(predaja == 0){
        cout << "PREDAJA";
    }

    return 0;
}