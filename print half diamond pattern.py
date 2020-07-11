'''
Print half diamond pattern using '*'. See example for more details.

Input Format

Input contains a single integer N.

Constraints

1 <= N <= 50

Output Format

For the given integer, print the half diamond pattern.

Sample Input 0

3
Sample Output 0

*
**
***
**
*
Explanation 0

Self Explanatory
'''

n=int(input())
for i in range(1,n+1):
    j='*'
    k=j*i
    print(k)
for l in range(2,i+1):
    i-=1
    l=j*i
    print(l)
