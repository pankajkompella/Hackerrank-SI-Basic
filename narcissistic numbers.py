'''
Given N, check whether it is a Narcissistic number or not. A narcissistic number is a number that is the sum of its own digits each raised to the power of the number of digits

Input Format

Input contains a integer - N.

Constraints

0 <= N <= 109

Output Format

Print "Yes" if the number is Narcissistic number, "No" otherwise.

Sample Input 0

8208
Sample Output 0

Yes
Explanation 0

84 + 24 + 04 + 84 = 8208
'''

n=str(input())
l=len(n)
#print(l)
ans=0
for i in n:
    #print(i)
    ans+=int(i)**l
    #print(ans)
#print(ans)
if ans==int(n):
    print('Yes')
else:
    print('No')
