/* 
Hackerrank problem
Summing the N series

Solution by Kyle Latino
*/

import java.io.scanner;

class Summing_the_N_series{

        // global vars
        int testCases;
        int input;
        
        // methods
        // find the sum of the series and print to stdout
        public int solve(int input){
                if (input<2){
                        return 1;
                }else{
                        return (input^2 - (solve(input-1))^2;
                }
        }
        
        // main function
        public static void main(String[] args){
        
                Scanner sc = new Scanner();
                testCases = sc.readInt();
                
                for(int i=0; i<testCases; i++){
                        input = sc.readInt();
                        System.out.println(solve(input));
                }
                
        }
}
