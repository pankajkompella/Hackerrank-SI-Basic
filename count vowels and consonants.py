'''
Given a string, print count of vowels and consonants of the string.

Input Format

Input contains a string of upperscase and lowercase characters - S.

Constraints

1 <= len(S) <= 100

Output Format

Print count of vowels and consonants for the given string, separated by space.

Sample Input 0

abxbbiaaspw
Sample Output 0

4 7
Explanation 0

Self Explanatory
'''

vow=['a','e','i','o','u','A','E','I','O','U']
# con=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
s=str(input())
v=0
c=0
for i in s:
    if i in vow:
        v+=1
    else:
        c+=1

print(v,c)
