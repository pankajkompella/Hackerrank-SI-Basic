/**
Find a duplicate element in the given array of integers. There will be only a single duplicate element in the array.
Note: Do not use any inbuilt functions/libraries for your main logic.

Input Format

First line of input contains size of the array - N and second line contains the elements of the array.

Constraints

2 <= N <= 100
0 <= ar[i] <= 109

Output Format

Print the duplicate element from the given array.

Sample Input 0

6
5 4 10 9 21 10
Sample Output 0

10
Explanation 0

Self Explanatory
**/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
    int i, j,n;
    long long a[300];
    scanf("%d", &n);
        for (i = 0; i < n; i++)
        scanf("%lld", &a[i]);
        for( i=0; i<n; i++)
        {
            for(j=i+1;j<n;j++)
            {
     if(a[i] == a[j])

     {printf("%lld",a[i]);
            break;}
        }
        }
}
