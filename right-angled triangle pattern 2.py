#YET TO BE SOLVED

'''
Print right-angled triangle pattern. See example for more details.

Input Format

First line of input contains a single integer N - the size of the triangle.

Constraints

1 <= N <= 50

Output Format

For the given integer, print the right-angled triangle pattern.

Sample Input 0

5
Sample Output 0

1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
Explanation:
In java 8;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        br.close();
        for(int i=1;i<=n;i++){
            int k=0;
            int l=n-1;
            for(int j=1;j<=i;j++){
                int s = i+k;
                System.out.print(s+" ");
                k+=l--;
            }
            System.out.println();
        }
    }
}

In python,
n = int(input())

for i in range(1,n+1):
    a,b = 0,n-1
    for j in range(1,i+1):
        print(i+a,end=" ")
        a+=b
        b-=1
    print()

Self Explanatory
'''

