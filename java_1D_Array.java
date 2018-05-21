/*
Hackerrank problem: Java 1D Array
Solution by: Kyle Latino

Objective:
Learn to manipulate 1 dementional arrays in java.

Read in values and save them to a java array. 
*/

import java.util.*;

public class Solution {

    public static void main(String[] args) {
	   
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        // create an int array capable of holding all values
        int[] a = new int[n];
        // iterate for each input value
        for(int i=0; i<n; i++){
            a[i] = scan.nextInt();
        }
        
        scan.close();

        // Prints each sequential element in array a
        for (int i = 0; i < a.length; i++) {
            System.out.println(a[i]);
        }
    }
}