/**
Given Number N. Print N!

Input Format

The input contains a number - N.

Constraints

0 <= N <= 20

Output Format

Print factorial of N.

Sample Input 0

3
Sample Output 0

6
Explanation 0

Self Explanatory
**/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main() 
{
    int n,ptr;
    long long factorial=1;
    scanf("%d",&n);
    for(ptr=1;ptr<=n;ptr++)
    {
        factorial*=ptr;
    }
    printf("%lld",factorial);
}
