'''
Given a string, check if it contains only digits.

Input Format

Input contains a string - S.

Constraints

1 <= len(S) <= 100

Output Format

Print "Yes" if string contains only digits, "No" otherwise.

Sample Input 0

123456786543
Sample Output 0

Yes
Explanation 0

Self Explanatory
'''

digits=['0','1','2','3','4','5','6','7','8','9']
n=str(input())
c=0
for i in n:
    if i not in digits:
        c+=1
    else:
        pass
if c!=0:
    print('No')
else:
    print('Yes')
