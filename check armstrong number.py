'''

Check whether a given number is Armstrong number.

Input Format

Input contains a integer - N.

Constraints

0 <= N <= 109

Output Format

Print "Yes" if the number is Armstrong number, "No" otherwise.

Sample Input 0

153
Sample Output 0

Yes
Explanation 0

13 + 53 + 33 = 153
'''

n=str(input())
cube=0
for i in n:
    cube+=(int(i))**3
#print(cube)
if cube==int(n):
    print('Yes')
else:
    print('No')
