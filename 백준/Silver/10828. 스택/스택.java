import java.io.*;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) throws IOException {
    	
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine()); //단어의 개수 N
        int count = N;
        
        LinkedList<Integer> list = new LinkedList<>();

        for (int i = 0; i < N; i++) {
            String str = br.readLine();

            if (str.startsWith("push")) {
            	 String numberPart = str.substring(5).trim(); // trim()은 앞뒤 공백을 제거
            	 
            	 if (!numberPart.isEmpty()) {
            	        int x = Integer.parseInt(numberPart);
            	        list.add(x);
            	 }
            	 
            }
            else if (str.equals("pop")) {
            	if(list.isEmpty()) {
            		System.out.println(-1);
            	}
            	else {
            		int x = list.pollLast();
                	
                	System.out.println(x);
               
            	}
            }
            else if (str.equals("size")) {
            	System.out.println(list.size());
            }
            else if (str.equals("empty")) {
            	if(list.isEmpty()) {
            		System.out.println(1);
            	}
            	else {
            		System.out.println(0);
            	}
            }
            else if (str.equals("top")) {
            	
            	if(list.isEmpty()) {
            		System.out.println(-1);
            	}
            	else {
            		System.out.println(list.getLast());
               
            	}
            	
            }

          
        }
        
    }

}