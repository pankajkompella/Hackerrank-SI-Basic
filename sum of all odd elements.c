/**
Print sum of all odd elements in an array.

Input Format

Input contains 2 lines, first line contains integer N - the size of the array and second line contains array elements.

Constraints

1 <= N <= 102
-106 <= ar[i] <= 106

Output Format

Print sum of all odd elements.

Sample Input 0

5
6 9 8 4 3
Sample Output 0

12
Explanation 0

Self Explanatory
**/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n,i;
    long a[100],sum=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%ld",&a[i]);
    
    }
    for(i=0;i<n;i++)
    {
        if(a[i]%2!=0)
        {
            sum=sum+a[i];
        }
    }
    printf("%ld",sum);
}
