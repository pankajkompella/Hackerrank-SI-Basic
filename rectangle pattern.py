'''
Print rectangle pattern. See example for more details.

Input Format

First line of input contains a single integer N - the size of the rectangle.

Constraints

1 <= N <= 50

Output Format

For the given integer, print rectangle pattern.

Sample Input 0

5
Sample Output 0

5432*
543*1
54*21
5*321
*4321
Explanation 0

Self Explanatory
'''

# n=int(input())
# for i in range(n):
#     for j in range(n-1):
#         print(n-j,end='')
#     print()
    
n = int(input())
s = 1
for i in range(n):
    for j in range(n,0,-1):
        if j == s :
            print('*',end = '')
        else:    
            print(j,end = '')
    s += 1
    print()    
