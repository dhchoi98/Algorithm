#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int slice, int n) {
    int answer = 0;
    answer = 1;
    while(n - (slice * answer) > 0){
        answer++;
    }
    return answer;
}