/**
Given N, print the sum of squares of 1st N natural numbers.

Input Format

Input contains positive integer - N.

Constraints

1 <= N <= 103

Output Format

Print the sum of squares of 1st N natural numbers.

Sample Input 0

15
Sample Output 0

1240
Explanation 0

Self Explanatory
**/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
long long n,i,sum=0;
    scanf("%lld",&n);
    for(i=1;i<=n;i++)
    {
        sum=sum+(i*i);
    }
    printf("%lld",sum);
}
