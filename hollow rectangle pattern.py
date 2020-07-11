'''
Print hollow rectangle pattern using '*'. See example for more details.

Input Format

Input contains two integers W and L. W - width of the rectangle, L - length of the rectangle.

Constraints

2 <= W <= 50 2 <= L <= 50

Output Format

For the given integers W and L, print the hollow rectangle pattern.

Sample Input 0

5 4
Sample Output 0

*****
*   *
*   *
*****
Explanation 0

Self Explanatory
'''

l,b=map(int,input().split())
print('*'*l)
for _ in range(b-2):
    print('*',' '*(l-4),'*')
print('*'*l)

'''
*****
*   *
*   *
*****
'''
