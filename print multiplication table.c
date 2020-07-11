/**
Print multiplication table for given integer - N.

Input Format

Input contains integer - N.

Constraints

-105 <= N <= 105

Output Format

Print multiplication table.

Sample Input 0

9
Sample Output 0

9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
9 * 10 = 90
Explanation 0

Self Explanatory
**/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

   int n,i;
    scanf("%d",&n);
    for(i=1;i<=10;i++)
    {
        printf("%d * %d = %d\n",n,i,n*i);
    }
}
