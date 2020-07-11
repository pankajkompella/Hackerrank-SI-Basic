'''
Print right-angled triangle pattern using palindrome strings. See example for more details.

Input Format

Input contains a integer N - lenght of the right angled triangle.

Constraints

1 <= N <= 26

Output Format

For the given integer N, print the right angled triangle.

Sample Input 0

5
Sample Output 0

A 
A B A 
A B C B A 
A B C D C B A 
A B C D E D C B A
Explanation 0

Self Explanatory
'''

n=int(input())
for i in range(1,n+1):
    for k in range(1,i+1):
        print(chr(k+65-1),end=' ')
    for l in range(i-1,0,-1):
        print(chr(l+65-1),end=' ')
    print()
