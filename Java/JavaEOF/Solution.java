import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int counter = 1;
        while(sc.hasNext()){
            System.out.printf("%d %s %n", counter, sc.nextLine());
            counter++;
        }
        
        sc.close();
        
    }
}