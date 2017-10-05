import java.io.*;
import java.util.*;

public class Summing_the_N_series {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int testCases = sc.nextInt();
        
        for(int i=0; i<testCases; i++){
            System.out.println(sum(sc.nextInt()));
        }
    }
    
    public static int sum(int n){
        if(n<2){
            return 1;
        }
        else{
            return (n^2 - (n-1)^2) + sum(n-1);
        }
    }
}
