#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    answer = 1;
    while((6 * answer) % n != 0) {
        answer++;
    }
    
    return answer;
}