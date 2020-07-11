/**
Check whether a given number is Armstrong number.

Input Format

Input contains a integer - N.

Constraints

0 <= N <= 109

Output Format

Print "Yes" if the number is Armstrong number, "No" otherwise.

Sample Input 0

153
Sample Output 0

Yes
Explanation 0

13 + 53 + 33 = 153
**/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
long long num,n,rem=0,cube=0,sum=0;
    scanf("%lld",&num);
    n=num;
    while(n!=0)
    {
        rem=n%10;
        cube=rem*rem*rem;
        sum=sum+cube;
        n=n/10;
    }
    if(sum==num)
    {
        printf("Yes");        
    }
    else
        printf("No");   
}
