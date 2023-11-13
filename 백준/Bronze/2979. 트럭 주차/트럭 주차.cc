#include<iostream>

using namespace std;
int timecnt[100]; //시간대 변수 (배열)인 time, 겹치는 시간을 0~3으로 기록


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int a, b, c;   
    int first[2];
    int second[2];
    int third[2]; 

    // 주차 요금 입력 받기
    cin >> a >> b >> c;
    
    // 3대의 차 각각 주차장 도착, 떠난 시각 입력 받기
    cin >> first[0] >> first[1];
    cin >> second[0] >> second[1];
    cin >> third[0] >> third[1];
    // 3대의 차가 동시에 몇 대 있었는지에 따라서 a, b, c의 요금이 동시간대에 추가가 됌.
    for(int i = 0; i < 100; i++){
        if(first[0] <= i && i < first[1] ){
            timecnt[i] = timecnt[i] + 1;
        }
        if(second[0] <= i && i < second[1] ){
            timecnt[i] = timecnt[i] + 1;
        }
        if(third[0] <= i && i < third[1] ){
            timecnt[i] = timecnt[i] + 1;
        }
    }

    // 최종 요금 출력
    int result = 0;
    for(int j = 0; j < 100; j++){
        if(timecnt[j] == 1){ // 1대 일때
            result = result + a;
        }
        else if(timecnt[j] == 2){ // 2대일 때
            result = result + (2 * b);
        }
        else if(timecnt[j] == 3){ // 3대일 때
            result = result + (3 * c);
        }
      
    }
    cout << result;


    return 0;
}