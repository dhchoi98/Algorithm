import java.util.*;


public class Main {
    public static void main(String[] args) {
        int fullDays; // n
        int days;     // k
        int degrees;
        int[] pSum = new int[100001];

        Scanner sc = new Scanner(System.in);

        fullDays = sc.nextInt();
        days = sc.nextInt();

        for(int i = 1; i <= fullDays; i++){
            degrees = sc.nextInt();
            pSum[i] = pSum[i - 1] + degrees;
        }
        int max = -10000004; // 온도 합 최댓값

        for(int j = days; j <= fullDays; j++){
            int sum = pSum[j] - pSum[j - days];
            if(sum > max)
                max = sum;
        }
        System.out.println(max);

    }
}
