package JavaStaticInitializerBlock;
import java.io.*;
import java.util.*;

public class Solution {
    static int b, h;
    static boolean flag = true;
    
    static{
        Scanner sc = new Scanner(System.in);
        b = sc.nextInt();
        h = sc.nextInt();
        if (b <= 0 || h <= 0){
            flag = false;
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        }
        sc.close();
    }

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        if(flag){
            System.out.printf("%d %n", b*h);
        }
    }
}