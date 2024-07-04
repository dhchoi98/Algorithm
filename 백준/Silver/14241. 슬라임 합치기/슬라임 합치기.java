import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int[] slime = new int[100];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 슬라임의 개수
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        // 슬라임의 크기
        for(int i = 0; i < n; i++) {
            slime[i] = Integer.parseInt(st.nextToken());

        }

        Arrays.sort(slime);
        int sum = 0;
        for(int j = 0; j < slime.length - 1; j++){
            for(int k = j + 1; k < slime.length; k++){
                sum += slime[j] * slime[k];
            }
        }
        System.out.print(sum);

    }


}
