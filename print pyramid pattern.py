'''
Print pyramid pattern. See example for more details.

Input Format

First line of input contains a single integer N - the size of the pyramid.

Constraints

1 <= N <= 50

Output Format

For the given integer, print pyramid pattern.

Sample Input 0

5
Sample Output 0

    *
   ***
  *****
 *******
*********
Explanation 0

Self Explanatory
'''

r=int(input())
c=0
for i in range(1,r+1):
    for j in range(1,(r-i)+1):
        print(end=" ")
    while c!=(2*i-1):
        print("*",end="")
        c+=1
    c=0
    print()
