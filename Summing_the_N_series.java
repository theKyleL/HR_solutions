import java.io.*;
import java.util.*;

public class Summing_the_N_series {

        // methods
        // find the sum of the series and print to stdout
        int solve(int input){
                if (input<2){
                        return 1;
                }else{
                        return (input^2 - (solve(input-1))^2);
                }
        }
        
        // main function
        public static void main(String[] args){
   
                Scanner sc = new Scanner(System.in);
                int testCases = sc.nextInt();
            
                for(int i=0; i<testCases; i++){
                        System.out.println(solve(sc.nextInt()));
                }
        }
}
