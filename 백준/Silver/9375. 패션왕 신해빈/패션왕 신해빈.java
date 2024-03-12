import java.util.*;
import java.io.*;




public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine()); // 테케 수
        int n = 0; // 의상 수



        for(int i = 0; i < t; i++) {
            n = Integer.parseInt(br.readLine());
            HashMap<String, Integer> hm = new HashMap<>(30);   // 이름, 종류

            int result = 1;
            for(int j = 0; j < n; j++){
                StringTokenizer st = new StringTokenizer(br.readLine(), " ");
                st.nextToken();
                String type = st.nextToken();
                hm.put(type, hm.getOrDefault(type, 0) + 1);

            }
            for(int val: hm.values()){
                result *= (val + 1);
            }
            System.out.println(result - 1);

        }
        

    }
}