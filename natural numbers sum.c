/**
Given positive integer - N, print the sum of 1st N natural numbers.

Input Format

Input contains a positive integer - N.

Constraints

1 <= N <= 104

Output Format

Print the sum of 1st N natural numbers.

Sample Input 0

4
Sample Output 0

10
Explanation 0

Self Explanatory
**/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    long sum=0,i,m;
    scanf("%ld",&m);
    for(i=1;i<=m;i++)
    {
        sum=sum+i;
    }
    printf("%ld",sum);
}
