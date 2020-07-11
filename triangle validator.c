/**
Given sides of a triangle, check whether the triangle is valid.

Input Format

Input contains three integers A, B, C - Sides of the triangle.

Constraints

1 <= A, B, C <= 109

Output Format

Print "Yes" if you can construct a triangle with the given three sides, "No" otherwise.

Sample Input 0

4 3 5
Sample Output 0

Yes
Explanation 0

Self Explanatory
**/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    long long  a,b,c,s1,s2,s3;
    scanf("%lld %lld %lld",&a,&b,&c);
    s1=a+b;
    s2=b+c;
    s3=a+c;
    if(s1>c && s2>a && s3>b)
        printf("Yes");
    else
        printf("No");
    
}
