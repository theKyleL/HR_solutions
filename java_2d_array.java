/*
Hackerrank problem: Java 2D Array
Solution by: Kyle Latino

Problem:
Given a 6x6 grid of numbers determine the sum of an 'hourglass' of values.

Hourglasses correspond to the positions of the numbers on a 2D array as follows:

1 1 1
  1  
1 1 1


*/

//boilerplate code (given)
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class java_2d_array{ /*Solution {*/



    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int[][] arr = new int[6][6];

        for (int i = 0; i < 6; i++) {
            String[] arrRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowItems[j]);
                arr[i][j] = arrItem;
            }
        }

        scanner.close();

        // calculate the largest hourglass sum
        System.out.println(findMaxSum(arr));

    }

    /* 
    Find the sum of the hourglass beginning at point x,y
    */
    private static int calcSum(int[][] arr, int x, int y){
    	int sum = 0;
    	for(int i=0; i<3; i=i+2){ // traverse the two rows w/ 3 points
    		for(int j=0; j<3; j++){
    			sum += arr[x+i][y+j];
    			// System.out.printf("%d\n", sum); // debug code
    		}
    	}
    	sum += arr[x+1][y+1]; // add the center point
    	return sum;
    }

    /*
    Traverse the 2D array and find the max hourglass sum
    */
    private static int findMaxSum(int[][] arr){
    	// initialize with a value from the array to enable results less than 0
    	int maxSum = calcSum(arr, 0, 0);
    	for(int i=0; i<4; i++){
    		for(int j=0; j<4; j++){
    			int temp = calcSum(arr, i, j);
    			// System.out.printf(" X: %d Y: %d = %d\n", i, j, temp); // debug code
    			if (temp > maxSum){
    				maxSum = temp;

    			}
    		}
    	}
    	return maxSum;
    }
}
