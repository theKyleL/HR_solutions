/*
Hackerrank problem: Java If-Else
Solution by: Kyle Latino

Problem:

Given an integer, , perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

*/

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        check(N);
        scanner.close();
    }
    
    private static void check(int n){
        if (n % 2 != 0){ // check for odd numbers
            System.out.println("Weird");
        }else if(n>1 && n<5){ // check for even numbers from 2-4
            System.out.println("Not Weird");
        }else if(n>5 && n<21){ // check for even numbers from 6-20
            System.out.println("Weird");
        }else if(n>20){ // check for even numbers greater than 20
            System.out.println("Not Weird");
        }
    }
}

