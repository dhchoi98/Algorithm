import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

//
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 재료의 개수
        int n = Integer.parseInt(br.readLine());

        // 갑옷을 만드는데 필요한 수
        int m = Integer.parseInt(br.readLine());

        // 재료의 고유한 번호들
        int[] material = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++){
            material[i] = Integer.parseInt(st.nextToken());
        }

        // 오름차순 정렬
        Arrays.sort(material);

        int count = 0;
        int i = 0;
        int j = n - 1;

        while(i < j){
            if(material[i] + material[j] < m){
                i++;    // i 와 j의 합이 m 보다 작으면 start 포인터 이동
            } else if (material[i] + material[j] > m){
                j--;    // i 와 j의 합이 m 보다 크면 end 포인터 이동
            } else{
                count++;  // 정답일 때
                i++;      // 두 포인터 모두 이동 (가운데 방향 으로)
                j--;
            }
        }
        System.out.println(count);
        br.close();
    }
}