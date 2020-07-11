/**
Find maximum element from the given array of integers.

Input Format:
First line of input contains N - the size of the array and second line contains the elements of the array.
Constraints:
1 <= N <= 103
-109 <= ar[i] <= 109
Output Format:
Print the maximum element of array.

Sample Input 0:
5
-2 -19 8 15 4
Sample Output 0:
15
Explanation 0:
Self Explanatory
**/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n,i,j,temp=0;
    long long a[1000];
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%lld",&a[i]);
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if(a[i]<a[j])
        {
            temp=a[i];
            a[i]=a[j];
            a[j]=temp;
        }
        }
    }
    printf("%lld",a[0]);
}
