class Solution {
    public StringBuilder solution(String my_string, int n) {
         StringBuilder answer = new StringBuilder();

        
        for(int j = 0; j < my_string.length(); j++){
            char a = my_string.charAt(j);
            for(int i = 0; i < n; i++) {
                answer.append(a);
            }
        }
        
        return answer;
    }
}