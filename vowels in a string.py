'''
Given a string, check if it contains only vowels.

Input Format

Input contains a string of lowercase and uppercase characters- S.

Constraints

1 <= len(S) <= 100

Output Format

Print "Yes" if string contains only vowels, "No" Otherwise.

Sample Input 0

askhtwsflk
Sample Output 0

No
Explanation 0

Self Explanatory
'''

n=str(input())
vowels=['A','E','I','O','U','a','e','i','o','u']
nope=0
for i in n:
    if i not in vowels:
        nope+=1
    else:
        pass
if nope==0:
    print('Yes')
else:
    print('No')
