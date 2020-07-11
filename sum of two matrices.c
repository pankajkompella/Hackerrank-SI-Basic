/**
Given two matrices A and B of size N x M. Print sum(A+B) of matrices(A, B).
Note: Try solving it by declaring only a single matrix.

Input Format

First line of input contains N, M - size of the matrices. Its followed by 2*N lines each containing M integers - elements of the matrices. First N lines for matrix A and its followed by N lines for matrix B.

Constraints

1 <= N, M <= 100
-106 <= ar[i] <= 106

Output Format

Print sum(A+B) of matrices(A, B).

Sample Input 0

2 3
5 -1 3
19 8 4
4 5 -6
1 -2 12
Sample Output 0

9 4 -3
20 6 16
Explanation 0

Self Explanatory.
**/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    long long a[100][100],b[100][100],c[100][100]={0};
    int i,j,n,m;
    scanf("%d %d",&n,&m);
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
          scanf("%lld",&a[i][j]);  
        }
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
          scanf("%lld",&b[i][j]);  
        }
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
          c[i][j]=a[i][j]+b[i][j]; 
        }
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
          printf("%lld ",c[i][j]);
            if(j==m-1)
                printf("\n");
        }
    }
}
