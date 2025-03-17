package JavaIntToString;
import java.io.*;
import java.util.*;

public class Solution {
    static int n;
    
    static{
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        sc.close();
    }

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        if(n >= -100 || n <= 100){
            System.out.println("Good job");
        }
    }
}