
import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
    
    
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	String s = br.readLine();
    	
    	int k = Integer.parseInt(s);
    	
    	Stack<Integer> stack = new Stack<>();
    	
    	for(int i = 0; i < k; i++) {
    		int num = Integer.parseInt(br.readLine());
    		if(num != 0) {
    			stack.push(num);
    		}
    		else {
    			stack.pop();
    		}
    	}
    	
    	int size = stack.size();
    	
    	int sum = 0;
    	for(int j = 0; j < size; j++) {
    		sum = sum + stack.pop();
    	}
    	System.out.println(sum);
    	
    }
    
}