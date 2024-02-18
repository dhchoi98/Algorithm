import java.util.*;
import java.io.*;



public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int n = sc.nextInt();
        String str = sc.next();

        StringTokenizer st = new StringTokenizer(str, "*");

        String a = st.nextToken();
        String b = "";
        if(st.hasMoreTokens()){
            b = st.nextToken();
        }

        for(int i = 0; i < n; i++){
            String file = sc.next();

            if(file.length() < a.length() + b.length()){
                sb.append("NE" + "\n");
                continue;
            }
            
            String front = file.substring(0, a.length());
            String back = file.substring(file.length() - b.length());
            

            if(front.equals(a) && back.equals(b)){
                sb.append("DA" + "\n");
            }
            else{
                sb.append("NE" + "\n");
            }
        }

        System.out.println(sb);

    }
}