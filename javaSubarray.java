/*
Hackerrank problem: Java Subarray
Solution by: Kyle Latino

Problem:

We define the following:
A subarray of an -element array is an array composed from a contiguous block of the original array's elements. For example, if , then the subarrays are , , , , , and . Something like  would not be a subarray as it's not a contiguous subsection of the original array.
The sum of an array is the total sum of its elements.
An array's sum is negative if the total sum of its elements is negative.
An array's sum is positive if the total sum of its elements is positive.
Given an array of  integers, find and print its number of negative subarrays on a new line.

*/

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class javaSubarray{

// public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */

        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        // create an int array capable of holding all values
        int[] a = new int[n];
        // iterate for each input value
        for(int i=0; i<n; i++){
            a[i] = scan.nextInt();
        }
        // System.out.println(String.format("New array length = %d", a.length));
        scan.close();

        traverseArrays(a, n);
    }

    /*
    Traverse the array and determine the number of subarrays that have a negative sum
    Input: int array
    Output: print int to stdout
    */
    public static void traverseArrays(int[] arr, int len){
    	// System.out.println("Entering traverseArrays method...");
    	int negativeSumArrays = 0;
    	// System.out.println(String.format("Array length = %d", arr.length)); // array needs to be 
 
    	/* calculate the number of possible subarrays (not necessary...)
    	[1] -> [1] = 1
    	[1, 2] -> [1] [2] [1, 2] =  3
    	[1, 2, 3] -> [1] [2] [3] [1, 2] [2, 3] [1, 2, 3] = 6
    	[1, 2, 3, 4] -> [1] [2] [3] [4] [1, 2] [2, 3] [3, 4] [1, 2, 3] [2, 3, 4] [1, 2, 3, 4] = 10
    	[1, 2, 3, 4, 5] = 15
    	
		numSubarrays(arr) = len(arr) + numSubarrays(arr-1)
    	*/

    	// traverse all subarrays and sum values
    	for (int i=1; i<=arr.length; i++){ // increment through the possible lengths of subarrays

    		// System.out.println(String.format("\nStarting outer loop.. i=%d", i));

    		for (int j=0; (j+i)<=arr.length; j++){ // increment through the possible 

    			// System.out.println(String.format("\nStarting inner loop.. j=%d", j));
    			
    			int sum = 0; 
    			int[] newArr = Arrays.copyOfRange(arr, j, j+i);
    			for (int x: newArr){
    				sum += x;
    				// System.out.println(String.format("Sum: %d", sum));
                }
    			if (sum<0){
    				negativeSumArrays += 1;
    				// System.out.println("Adding 1 to negativeSumArrays");
    			}

    		}
    	}
    	System.out.println(negativeSumArrays);
    }
}

