import java.util.*;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        // array 의 길이는 홀수
        Arrays.sort(array); 
        int length = array.length;
        answer = array[length / 2];
        
        return answer;
    }
}