import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int q = in.nextInt();
        for(int i=0;i<q;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            
            int currentValue = a;
            int multiplier = 1;
            StringBuilder series = new StringBuilder();
            for(int j = 0; j < n ; j++){
                currentValue += multiplier * b;
                series.append(currentValue).append(' ');
                multiplier *= 2;
            }
            System.out.println(series.toString().trim());
        }
        in.close();
    }
}


public static class Solution {
    public static void main(String[] args) {
        // Step 1: Read input
        Scanner scanner = new Scanner(System.in);
        int q = scanner.nextInt();  // Number of queries

        // Step 2: Process each query
        for (int i = 0; i < q; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int n = scanner.nextInt();

            // Step 3: Generate the series
            int currentValue = a;
            StringBuilder series = new StringBuilder();

            for (int j = 0; j < n; j++) {
                currentValue += (int) Math.pow(2, j) * b;  // Using Math.pow()
                series.append(currentValue).append(" ");
            }

            // Step 4: Print the result
            System.out.println(series.toString().trim());  // Trim removes trailing space
        }

        scanner.close();
    }
}

// Comparison:
// Approach	Performance	Pros	Cons
// Using Math.pow(2, j)	
// O(n)	Simple and readable	Casting from double to int is needed
// Using a multiplier (multiplier *= 2)	
// O(n)	More efficient	Slightly more code
// Which Approach is Better?
// Using a multiplier (multiplier *= 2) is slightly faster than Math.pow(2, j), since:
// Math.pow() uses floating-point operations, while multiplier *= 2 just doubles an integer.
// Floating-point operations can be slower and less precise for large values.
// If performance matters, go with the multiplier approach. Otherwise, Math.pow(2, j) is fine for readability.