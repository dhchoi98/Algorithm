import java.io.*;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) throws IOException {
    
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	String str = br.readLine();
    	int count = 0;
    	
    	for(int i = 0; i < str.length(); i++) {
    		char current = str.charAt(i);
    		
    		switch (current) {
    			case 'c' :
    				try {
	    				if(str.charAt(i + 1) == '=' || str.charAt(i + 1) == '-') {
	    					i++;
	    				}
    				} catch (StringIndexOutOfBoundsException e) {
    		            
    		        }
    				
    				break;
    			case 'd' :
    				try {
    					if(str.charAt(i + 1) == '-' )
    					{
    						i++;
    					}
    					else if(str.charAt(i + 1) == 'z' && str.charAt(i + 2) == '=') {
    						i = i + 2;
    					}
    				} catch (StringIndexOutOfBoundsException e) {
    		            
    		        }
    				
    				break;
    				
    			case 'l' :
    				try {
    					if(str.charAt(i + 1) == 'j')
    					{
    						i++;
    					}
    					
    				} catch (StringIndexOutOfBoundsException e) {
    		            
    		        }
    				
        				
    				break;
    			case 'n' :
    				try {
    					if(str.charAt(i + 1) == 'j')
    					{
    						i++;
    					}
    					
    				} catch (StringIndexOutOfBoundsException e) {
    		            
    		        }
        			
    				break;
    			case 's' :
    				
    				try {
    					if(str.charAt(i + 1) == '=')
    					{
    						i++;
    					}
    					
    				} catch (StringIndexOutOfBoundsException e) {
    		            
    		        }
        		
    				break;
    			case 'z' :
    				
    				try {
    					if(str.charAt(i + 1) == '=')
    					{
    						i++;
    					}
    					
    				} catch (StringIndexOutOfBoundsException e) {
    		            
    		        }
    				
    				break;
    			default : // 나머지 알파벳
    				
    				break;
    				
    		}
    		count++;
    	}
    	
    	System.out.println(count);
    
    }

}