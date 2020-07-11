/**
Given a matrix of size N x M. Print whether it is a sparse matrix. A matrix containing 0 value in more than half of its elements, then it is called a sparse matrix.

Input Format

First line of input contains N, M - size of the matrix. Its followed by N lines each containing M intergers - elements of the matrix.

Constraints

1 <= N, M <= 100
0 <= ar[i] <= 109

Output Format

Print "Yes" if given matrix is Sparse matrix, otherwise print "No".

Sample Input 0

2 3
5 0 0
0 8 0
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

    int i,j,m,n,count=0;
    long long a[100][100];
    scanf("%d %d",&n,&m);
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
     for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(a[i][j]==0)
            {
                count=count+1;
            }
        }
    }
   int d=(n*m)/2;
    if(count>d)
        printf("Yes");
    else
        printf("No");
}
