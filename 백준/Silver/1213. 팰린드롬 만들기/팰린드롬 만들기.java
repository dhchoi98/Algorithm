import java.io.*;

//p1213
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        int[] alpha = new int[26];

        for(int i=0; i< s.length(); i++) {
            int idx = s.charAt(i)-'A';
            alpha[idx]++;
        }

        int isOne = 0;
        // 펠린 드롬이 안되는 경우 : 홀수 알파벳이 2개 이상일 경우
        for(int j = 0; j < 26; j++) {
            if(alpha[j] % 2 != 0){
                isOne++;
            }
        }
        String answer = "";
        StringBuilder sb = new StringBuilder();
        if(isOne > 1){
            answer += "I'm Sorry Hansoo";
        }else{
            // Z부터 안 쪽에다 붙여야 오름차 순 으로 정렬됨
            for(int i=0; i<alpha.length; i++) {
                for(int r=0; r<alpha[i]/2; r++) {
                    sb.append((char)(i+65));
                }
            }
            answer += sb.toString();
            String end = sb.reverse().toString();

            sb = new StringBuilder();
            for(int i=0; i<alpha.length; i++) {
                if(alpha[i] % 2 == 1) {
                    sb.append((char)(i+65));
                }
            }
            answer += sb.toString()+end;

        }

        System.out.println(answer);

    }
}